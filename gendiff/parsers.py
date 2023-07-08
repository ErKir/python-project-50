#!/usr/bin/env python3

import yaml
import json


EXTENSIONS = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
}


def parse(path):
    name_parts = path.split('.')
    extension = name_parts[len(name_parts) - 1].lower()
    data = open(path)
    if extension not in EXTENSIONS:
        raise ValueError('Unsupported format. Next formats are supported: {}'
                         .format(EXTENSIONS.keys()))
    return EXTENSIONS[extension](data)
