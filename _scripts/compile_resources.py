# -*- coding: utf-8 -*-
"""."""

import pathlib
import subprocess

APP_NAME = 'br.com.justcode.Qt'

BASE_DIR = pathlib.Path(__file__).resolve().parent

INPUT = BASE_DIR.parent / 'resources' / 'resources.qrc'
OUTPUT = BASE_DIR.parent / 'app_pyside' / 'resources_rc.py'


def main() -> None:
    compile_resources()


def compile_resources() -> None:
    print('[!] Generating resources_rc.py, please wait... [!]')
    subprocess.run(args=['pyside6-rcc', INPUT, '-o', OUTPUT], check=False)
    print('[!] Done [!]')


if __name__ == '__main__':
    main()
