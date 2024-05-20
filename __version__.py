# -*- coding: utf-8 -*-
"""."""

from datetime import datetime


def get_version() -> str:
    return f'{datetime.now():%Y.%m.%d.%f}'


if __name__ == "__main__":
    print(get_version())
