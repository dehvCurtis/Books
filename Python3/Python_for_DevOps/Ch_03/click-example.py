#! /usr/bin/env python
"""
CLI tool for using click
"""
import click

@click.group()
def cli():
    pass

@click.group(help='Ship related commands')
def ships():
    pass

cli.add_command(ships)

@ships.command(help='Sail a ship')
def sail():
    ship_name = 'Your ship'
    print(f'{ship_name} is setting sail')

@ships.sai