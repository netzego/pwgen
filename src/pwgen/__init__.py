import os
import sys

import click

__version__ = (0, 0, 0)


@click.command()
def main():
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
