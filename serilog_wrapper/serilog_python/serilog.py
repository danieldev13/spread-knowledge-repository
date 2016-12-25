import requests
import json
import enum
import settings


headers = {'api-key': settings.serilog_api_key, 'Content-type': 'application/json', 'Accept': 'text/plain'}


def error(ex, message):
    """
    Posts error data to Serilog Wrapper
    :param ex: exception risen
    :param message: readable message
    """
    try:
        payload = {'message': message, 'exceptionData': ex.args[0], 'logType': LogType.Error}
        requests.post(settings.serilog_api_url, data=json.dumps(payload), headers=headers)
    except:
        pass


def information(message):
    """
    Posts information data to Serilog Wrapper
    :param message: readable message
    """
    try:
        payload = {'message': message, 'exceptionData': {}, 'logType': LogType.Information}
        requests.post(settings.serilog_api_url, data=json.dumps(payload), headers=headers)
    except:
        pass


def fatal(ex, message):
    """
    Posts fatal data to Serilog Wrapper
    :param ex: exception risen
    :param message: readable message
    """
    try:
        payload = {'message': message, 'exceptionData': ex.args[0], 'logType': LogType.Fatal}
        requests.post(settings.serilog_api_url, data=json.dumps(payload), headers=headers)
    except:
        pass


def warning(ex, message):
    """
    Posts warning data to Serilog Wrapper
    :param ex: exception risen
    :param message: readable message
    """
    try:
        payload = {'message': message, 'exceptionData': ex.args[0], 'logType': LogType.Warning}
        requests.post(settings.serilog_api_url, data=json.dumps(payload), headers=headers)
    except:
        pass


def debug(ex, message):
    """
    Posts debug data to Serilog Wrapper
    :param ex: exception risen
    :param message: readable message
    """
    try:
        payload = {'message': message, 'exceptionData': ex.args[0], 'logType': LogType.Debug}
        requests.post(settings.serilog_api_url, data=json.dumps(payload), headers=headers)
    except:
        pass


class LogType(enum.Enum):
    """
    Enumeration representing the log types.
    """
    Information = 0,
    Error = 1,
    Warning = 2,
    Debug = 3,
    Fatal = 4
