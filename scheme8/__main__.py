from __future__ import print_function
from jsonschema import Draft7Validator
import argparse
import json
import os
import pkg_resources
import sys
import yaml


def main():
    """Scheme8 Linter"""
    parser = argparse.ArgumentParser(prog="scheme8")
    parser.add_argument(
        "--version",
        action="version",
        version=pkg_resources.get_distribution("scheme8").version,
    )
    parser.add_argument("file", nargs="+", help="file(s) to lint")
    args = parser.parse_args()


if __name__ == "__main__":
    main()
