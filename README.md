# Library shows difference between two configuration files and shows a difference

[![Actions Status](https://github.com/ErKir/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/ErKir/python-project-50/actions)[![Maintainability](https://api.codeclimate.com/v1/badges/24934b800a309cd750f8/maintainability)](https://codeclimate.com/github/ErKir/python-project-50/maintainability)[![Test Coverage](https://api.codeclimate.com/v1/badges/24934b800a309cd750f8/test_coverage)](https://codeclimate.com/github/ErKir/python-project-50/test_coverage)

Project description: The project implements the function of comparing **json** or **yaml** files and outputting the difference in different formats.

## Get started

Clone the repository and use `make package-install` command.
For help use `gendiff -h` command.

For comparison, use the following command `gendiff filepath1 filepath2`
the library will return the difference between files in the default format *stylish*
To return the result in a different format, use the `--format` flag and the format name,
the following formats are available: *plain*, *json* and also *stylish* as default.

For example: `gendiff --format plain filepath1 filepath2`

### Compare two simple JSON files

[![asciicast](https://asciinema.org/a/4Ckelr0SsGcgulWL7JWSp9xnL.svg)](https://asciinema.org/a/4Ckelr0SsGcgulWL7JWSp9xnL)

### Compare two simple YAML files

[![asciicast](https://asciinema.org/a/2l2LuXXOIRHlTl1d48pjaX6Nv.svg)](https://asciinema.org/a/2l2LuXXOIRHlTl1d48pjaX6Nv)

### Example of working with nested structures JSON or YAML files

[![asciicast](https://asciinema.org/a/bw6RyqrfXXFztIhaxnMowagJ1.svg)](https://asciinema.org/a/bw6RyqrfXXFztIhaxnMowagJ1)

### Example of working with "plain" formatter for JSON or YAML files

[![asciicast](https://asciinema.org/a/P0XWojumoI3g5q8phEg0k5Fy9.svg)](https://asciinema.org/a/P0XWojumoI3g5q8phEg0k5Fy9)

### Example of working with "json" formatter for JSON or YAML files

[![asciicast](https://asciinema.org/a/RuDOkHqFuiigUR12d1l3xznLx.svg)](https://asciinema.org/a/RuDOkHqFuiigUR12d1l3xznLx)
