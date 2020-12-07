#!/usr/bin/env python

import fire

def greet(greeting='Hi',name='Tammy'):
    print(f'{greeting} {name}')

if __name__ == "__main__":
    fire.Fire(greet)