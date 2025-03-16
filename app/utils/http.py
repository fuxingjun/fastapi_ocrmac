import re


def convert_to_camelcase(key):
    return re.sub(r"_([a-zA-Z])", lambda match: match.group(1).upper(), key)


def convert_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower().strip('_')


def http_success(data):
    return {
        "code": 0,
        "data": data,
        "message": "",
    }


def http_fail(message, code=1, data=None):
    return {
        "code": code,
        "data": data,
        "message": message,
    }
