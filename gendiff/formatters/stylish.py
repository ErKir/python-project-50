#!/usr/bin/env python3

CHANGES = {
    'unchanged': '  ',
    'removed': '- ',
    'added': '+ ',
}


def get_indents(level):
    count = 2
    replacer = '  '
    indent_size = level * count
    current_space = replacer * (indent_size - 1)
    bracket_space = replacer * (indent_size - count)
    return {
        "current_indent": current_space,
        "bracket_indent": bracket_space,
    }


def serialize(v):
    match v:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return v


def stringify(value, level):
    if type(value) is dict:
        result = '{'
        current_indent, bracket_indent = get_indents(level).values()
        for key, val in value.items():
            result += f'\n{current_indent}  {key}: {stringify(val, level + 1)}'
        result += f'\n{bracket_indent}'
        result += '}'
        return result
    return f'{serialize(value)}'


def stylish(diff, deep=1):
    current_indent, bracket_indent = get_indents(deep).values()
    result = '{\n'
    for item in diff:
        state = item['state']
        if state == 'nested':
            name, state, children = item.values()
            result += f'{current_indent}  {name}: '
            result += f'{stylish(children, deep + 1)}\n'
        elif state == 'updated':
            name, value1, value2, state = item.values()
            result += f'{current_indent}{CHANGES["removed"]}{name}: '
            result += f'{stringify(value1, deep + 1)}\n'
            result += f'{current_indent}{CHANGES["added"]}{name}: '
            result += f'{stringify(value2, deep + 1)}\n'
        else:
            name, value1, state = item.values()
            result += f'{current_indent}{CHANGES[state]}{name}: '
            result += f'{stringify(value1, deep + 1)}\n'

    result += f'{bracket_indent}'
    result += '}'
    return result
