#!/usr/bin/env python

import argparse

def sail():
    ship_name = 'Tallihoe'
    print(f'{ship_name} is setting sail')

def list_ships():
    ships = ['John B','Yankee','Pequod','Maria']
    print(f'Ships: {ships}')

def greet(greeting,name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Maritime Control')

    parser.add_argument('--twice','-t',help='Do it twice',action='store_true')

    subparsers = parser.add_subparsers(dest='func')

    