import datetime
from enum import Enum

import jwt
from flask import current_app


class TokenBase:
    def dump(self) -> dict:
        raise NotImplementedError

    @classmethod
    def load(cls, payload: dict):
        raise NotImplementedError

    def encode(self, *, exp: datetime.timedelta=None) -> str:
        payload = self.dump()
        if exp is not None:
            payload.update({'exp': (datetime.datetime.now() + exp).timestamp()})
        return bytes.decode(jwt.encode(payload, key=current_app.config['SECRET_KEY']))

    @classmethod
    def decode(cls, token: str):
        try:
            return cls.load(jwt.decode(str.encode(token), key=current_app.config['SECRET_KEY']))
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return None


class EmailConfirmationType(Enum):
    Registration = 0
    Changing = 1


class EmailConfirmationToken(TokenBase):
    def __init__(self, confirmation_type: EmailConfirmationType, user_id, email):
        self.type = confirmation_type
        self.user_id = user_id
        self.email = email

    def dump(self) -> dict:
        return {
            'type': self.type.value,
            'uid': self.user_id,
            'email': self.email
        }

    @classmethod
    def load(cls, payload: dict):
        return cls(
            confirmation_type=EmailConfirmationType(payload['type']),
            user_id=payload['uid'],
            email=payload['email']
        )


class PasswordRecoveryToken(TokenBase):
    def __init__(self, user_id):
        self.user_id = user_id

    def dump(self) -> dict:
        return {'uid': self.user_id, 't': 'recovery'}

    @classmethod
    def load(cls, payload: dict):
        return cls(user_id=payload['uid']) if payload['t'] == 'recovery' else None
