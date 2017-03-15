# -*- coding: utf-8 -*-

import click
from . import steve01


@click.command()
def main(args=None):
    """Console script for steve01"""
    #click.echo("Replace this message by putting your code into "
    #           "steve01.cli.main")
    #click.echo("See click documentation at http://click.pocoo.org/")
    steve01.main()


if __name__ == "__main__":
    main()
