import re


def replace_invalid_chars(text):
    return re.sub('(\r\n?|\n)+|(-9999999999)', '', text).strip()


def format_as_number(text):
    return re.sub(',', '.', re.sub(r'\.', '', replace_invalid_chars(text)))


def replace_non_numeric_chars(text):
    return re.sub(r'[^\d]', '', replace_invalid_chars(text))
