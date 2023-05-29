import time
from enum import IntEnum

DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class LogLevel(IntEnum):
    ERROR = 1
    INFO = 2
    DEBUG = 3


LOG_LEVEL = LogLevel.DEBUG


def log_error(text):
    log(text, LogLevel.ERROR)


def log(text, level: LogLevel):
    if level <= LOG_LEVEL:
        print('[%s] %s - %s' % (time.strftime(DATE_TIME_FORMAT), level.name, text))
