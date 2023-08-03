#!/usr/bin/env python3
"""obfuscate data from a log file"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = None):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields if fields else []

    def filter_datum(self, fields: List[str],
                     redaction: str, message: List[str],
                     separator: str) -> str:
        """return the log message obfuscated"""
        for i in fields:
            message = re.sub(i + "=.*?" + separator,
                             i + "=" + redaction + separator, message)
        return message

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum"""
        record.asctime = self.formatTime(record, self.datefmt)
        record.msg = self.filter_datum(self.fields, self.REDACTION,
                                       record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
