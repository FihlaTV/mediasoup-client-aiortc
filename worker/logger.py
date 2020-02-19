import logging
import sys

_rootLogger = logging.getLogger()
_rootLogger.addHandler(logging.StreamHandler(sys.stdout))
_debugLogger = logging.Logger('')
_debugLogger.addHandler(logging.StreamHandler(sys.stdout))
_errorLogger = logging.Logger('')
_errorLogger.addHandler(logging.StreamHandler(sys.stderr))


class Logger:
    @staticmethod
    def setLogLevel(logLevel: str):
        _rootLogger.setLevel(logLevel.upper())
        _debugLogger.setLevel(logLevel.upper())
        _errorLogger.setLevel(logLevel.upper())

    @staticmethod
    def debug(*args):
        _debugLogger.debug(*args)

    @staticmethod
    def warning(*args):
        _errorLogger.warning(*args)

    @staticmethod
    def error(*args):
        _errorLogger.error(*args)
