#!/usr/bin/env python3

import yaml
import json


EXTENSIONS = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
}


def parse(file, extension):
    if extension not in EXTENSIONS:
        raise ValueError('Unsupported format. Next formats are supported: {}'
                         .format(EXTENSIONS.keys()))
    return EXTENSIONS[extension](file)
