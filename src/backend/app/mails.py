from urllib import parse as urlparse

from threading import Thread
from flask import render_template, current_app
from flask_mail import Message
from werkzeug.datastructures import FileStorage

from app.extensions import mail


def email_confirmation_url(token):
    frontend_url = current_app.config['SCHEME']+'://'+current_app.config['FRONTEND_URL']
    email_confirmation_path = current_app.config['FRONTEND_EMAIL_CONFIRM_URL']
    full_url = urlparse.urljoin(frontend_url, email_confirmation_path)

    url_parts = list(urlparse.urlparse(full_url))

    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update({
        'token': token
    })
    url_parts[4] = urlparse.urlencode(query)
    return urlparse.urlunparse(url_parts)


def password_reset_url(token):
    frontend_url = current_app.config['SCHEME']+'://'+current_app.config['FRONTEND_URL']
    password_reset_path = current_app.config['FRONTEND_PASSWORD_RESET_URL']
    full_url = urlparse.urljoin(frontend_url, password_reset_path)

    url_parts = list(urlparse.urlparse(full_url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update({
        'token': token
    })
    url_parts[4] = urlparse.urlencode(query)
    return urlparse.urlunparse(url_parts)

def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(email: str, subject: str, message: str, *, sender=None, attachment: FileStorage=None):
    msg = Message(
        sender=sender,
        subject=subject,
        recipients=[email],
        html=message,
    )
    if attachment is not None:
        msg.attach(attachment.filename, attachment.content_type, attachment.stream.read())
    app = current_app._get_current_object()
    thr = Thread(target=send_async_mail, args=[app,msg])
    thr.start()
    # mail.send(msg)


def send_registration_email(email: str, fullname: str, token: str):
    send_mail(
        email=email,
        subject='Registration on SFT',
        message=render_template(
            template_name_or_list='registration.html',
            fullname=fullname,
            token=token, secret_url=email_confirmation_url(token)
        )
    )


def send_password_recovery_email(email: str, fullname: str, token: str):
    send_mail(
        email=email,
        subject='Password recovery on SFT',
        message=render_template(
            template_name_or_list='password_recovery.html',
            fullname=fullname,
            token=token, secret_url=password_reset_url(token)
        )
    )


def send_email_changing_email(email: str, fullname: str, token: str):
    send_mail(
        email=email,
        subject='Email changing on SFT',
        message=render_template(
            template_name_or_list='email_changing.html',
            fullname=fullname,
            token=token, secret_url=email_confirmation_url(token)
        )
    )


def send_feedback(from_email: str, name: str, topic: str, message: str, attachment=None):
    send_mail(
        sender=from_email,
        email=current_app.config['MAIL_FEEDBACK'],
        subject=f'Feedback: {topic}',
        message=render_template('feedback.html', fullname=name, message=message),
        attachment=attachment
    )