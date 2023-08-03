#!/usr/bin/env python3
"""obfuscate data from a log file"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: List[str], separator: str) -> str:
    """return the log message obfuscated"""
    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator, message)
    return message
