#!/usr/bin/env python3
"""Auth module"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Takes in a password string arguments and returns bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Instance of Auth class.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers and returns a new user if email isn't listed.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
