import datetime

import click
from flask.cli import AppGroup

from app.authorization.permissions import SPECIAL_ACTIONS
from database import db
from database.models import User, UserCredentials, ProfilePermission

superuser_cli = AppGroup('superuser')


@superuser_cli.command('create', with_appcontext=True)
@click.argument('name')
@click.argument('email')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def superuser_create(name, email, password):
    superuser = User(
        fullname=name,
        credentials_backref=UserCredentials(
            email=email,
            password=password,
            is_email_confirmed=True
        ),
        permissions_backref=[
            ProfilePermission(
                name=action.value, is_allowed=True,
                granted_at=datetime.datetime.now()
            )
            for action in SPECIAL_ACTIONS
        ],
        registered_at=datetime.datetime.now(),
    )
    db.session.add(superuser)
    db.session.commit()

    click.echo(f'SuperUser "{name}" with email "{email}" is successfully created')
