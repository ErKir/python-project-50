#!/usr/bin/env python3

import yaml
import json


EXTENSIONS = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
}


def parse(path):
    normalized_name = path.lower()
    extension = normalized_name.split('.')[1]
    data = open(path)
    if extension not in EXTENSIONS:
        raise ValueError('Unsupported format. Next formats are supported: {}'
                         .format(EXTENSIONS.keys()))
    return EXTENSIONS[extension](data)
