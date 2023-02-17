# csv.py
"""csv example."""

import sys
import csv


def data(filename):
    """Return the data from the file."""
    with open(filename, 'r') as f:
        lines = []
        for record in csv.DictReader(f):
            lines.append(record)
        return lines


filename = sys.argv[1]
print(data(filename))
