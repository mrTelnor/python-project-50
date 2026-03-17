import argparse
from importlib.metadata import PackageNotFoundError, version

from gendiff import generate_diff

try:
    VERSION = version("hexlet-code")
except PackageNotFoundError:
    VERSION = "unknown"


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument(
        '-f', '--format',
        default='stylish',
        choices=['stylish', 'plain', 'json'],
        help='set format of output'
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'%(prog)s {VERSION}',
        help='show program version'
    )

    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
