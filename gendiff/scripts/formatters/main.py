#!/usr/bin/env python3
from gendiff.scripts.formatters.stylish import to_string

# Cоздать словарь для выбора функций стиля
# {
#     'stylish': to_string(),
#     'plain': to_string()
# }


def formatted(diff, style):

    if style == 'stylish':
        return to_string(diff)
