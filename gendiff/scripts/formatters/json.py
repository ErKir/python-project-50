#!/usr/bin/env python3
import json


def jsonify(result):
    result = sorted(result, key=lambda x: x["name"])
    result = json.dumps(result)
    return result
