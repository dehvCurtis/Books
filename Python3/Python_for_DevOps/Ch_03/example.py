#! /usr/bin/env python
"""Simple click example"""

from typing import DefaultDict
import click

@click.command()
@click.option('--greeting', default='Hey There')
@click.option('--name', default='Tammy')

def greet(greeting, name):
    print(f'{greeting} {name}')

if __name__ == '__main__':
    greet()