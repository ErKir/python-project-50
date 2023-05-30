#!/usr/bin/env python3

import yaml
import json


def parse(path):
    normalized_name = path.lower()
    if normalized_name.endswith('json'):
        return json.load(open(path))
    else:
        return yaml.load(open(path))
