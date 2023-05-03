#!/usr/bin/env python3
import json

def generate_diff(first_file, second_file, format):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))