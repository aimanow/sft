import os
import uuid
from enum import Enum
from http import HTTPStatus

import flask
import jwt
from flask import current_app, redirect, url_for
from flask_restplus import abort

from app.api.namespaces import blueprint


class FileCategory(Enum):
    AvatarImage = 0
    AspectImage = 1
    DiscussionImage = 2
    Attachment = 3
    EducationScan = 4


DIRECTORY_OF = {
    FileCategory.AvatarImage: 'avatars',
    FileCategory.AspectImage: 'aspects',
    FileCategory.DiscussionImage: 'discussions',
    FileCategory.Attachment: 'attachments',
    FileCategory.EducationScan: 'educations',
}

PRESERVE_FILENAME_FOR = [
    FileCategory.Attachment
]


class FileToken:
    def __init__(self, category: FileCategory, path):
        self.category = category
        self.path = path

    def encode(self) -> str:
        return bytes.decode(jwt.encode(key=current_app.config['SECRET_KEY'], payload={
            't': self.category.value,
            'p': self.path
        }))

    @staticmethod
    def decode(token) -> "FileToken":
        payload = jwt.decode(str.encode(token), key=current_app.config['SECRET_KEY'])
        return FileToken(path=payload['p'], category=FileCategory(payload['t']))


def create_file_path(category: FileCategory, relative_path):
    path = current_app.config['UPLOAD_FOLDER']

    path = os.path.join(path, DIRECTORY_OF[category], relative_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


@blueprint.route('/files/<string:token>/<string:filename>')
def download_file(token, filename):
    file_token = FileToken.decode(token)
    if filename != os.path.basename(file_token.path):
        return abort(HTTPStatus.NOT_FOUND, message='File is not found')
    path = create_file_path(file_token.category, file_token.path)
    return flask.send_from_directory(os.path.dirname(path), os.path.basename(path))


def download_link(category: FileCategory, relative_path):
    token = FileToken(category, relative_path)
    return url_for(
        endpoint='api.download_file',
        token=token.encode(),
        filename=os.path.basename(token.path)
    )


def download(category: FileCategory, relative_path):
    return redirect(download_link(category, relative_path))


def upload(category: FileCategory, file) -> FileToken:
    if category in PRESERVE_FILENAME_FOR:
        relative_path = os.path.join(str(uuid.uuid4()), file.filename)
    else:
        extension = os.path.splitext(file.filename)[1]
        relative_path = str(uuid.uuid4()) + extension

    file.save(create_file_path(category, relative_path))
    return FileToken(category, relative_path)
