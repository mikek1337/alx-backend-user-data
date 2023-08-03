#!/usr/bin/env python3
"""encrypt password module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """return a salted, hashed password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
