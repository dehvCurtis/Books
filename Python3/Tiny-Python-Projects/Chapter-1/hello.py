#!/usr/bin/env python3
"""
Purpose: Say hello
"""

import argparse

# ---------------------
def get_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("-n",
                        "--name",
                        metavar="name",
                        default="World",
                        help="Name to greet")
    return parser.parse_args()

# ---------------------
def main():
    """Main fire"""
    args = get_args()
    print(f"Hello, {args.name}!")

# ---------------------
if __name__ == "__main__":
    main()
