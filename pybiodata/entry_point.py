#!/usr/bin/env python

import sys

from .base import AbstractDatabase
from .pdb import PDB


def main():
    try:
        assert len(sys.argv) > 1
        dbname = sys.argv[1]
        assert dbname in ['PDB',]
    except AssertionError:
        parser = AbstractDatabase.set_command_arguments()
        print(parser.print_help(sys.stderr))
        sys.exit(1)

    if dbname == 'PDB':
        parser = PDB.set_command_arguments()
        db = PDB(parser)
    db.run()
