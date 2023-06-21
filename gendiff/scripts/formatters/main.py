#!/usr/bin/env python3
from gendiff.scripts.formatters.stylish import stylish
from gendiff.scripts.formatters.plain import plain


def formatted(diff, style):
    match style:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
