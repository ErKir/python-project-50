#!/usr/bin/env python3
from gendiff.scripts.formatters.stylish import stylish
from gendiff.scripts.formatters.plain import plain
from gendiff.scripts.formatters.json import jsonify


def formatted(diff, style):
    match style:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return jsonify(diff)
