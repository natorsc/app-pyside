# -*- coding: utf-8 -*-
"""."""

import pathlib
import subprocess

APP_NAME = 'br.com.justcode.Qt'

BASE_DIR = pathlib.Path(__file__).resolve().parent
PROJ_DIR = BASE_DIR.parent / 'app_pyside'
LOCALES_DIR = BASE_DIR.parent / 'resources' / 'locales'

SOURCE_LANGUAGE = 'pt_BR'
TARGET_LANGUAGES = ['en_US']


def main() -> None:
    create_or_update_translations()
    compile_translations()


def create_or_update_translations() -> None:
    print('[!] Updating the translations (*.ts), please wait... [!]')
    for lang in TARGET_LANGUAGES:
        output = LOCALES_DIR.joinpath(lang, f'{APP_NAME}.{lang}.ts')
        output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            args=[
                'pyside6-lupdate',
                '-no-obsolete',
                '-extensions',
                'py',
                '-source-language',
                SOURCE_LANGUAGE,
                '-target-language',
                lang,
                PROJ_DIR,
                '-ts',
                output,
            ],
            check=False,
        )
    print('[!] Done [!]')


def compile_translations() -> None:
    print('[!] Compiling the translations (*.qm), please wait... [!]')
    for file in LOCALES_DIR.rglob('*.ts'):
        if file.is_file() and file.suffix == '.ts':
            output = file.parent.joinpath(f'{file.stem}.qm')
            subprocess.run(
                args=['pyside6-lrelease', file, output],
                check=False,
            )
    print('[!] Done [!]')


if __name__ == '__main__':
    main()
