#!/bin/python3

import os
import sys
import subprocess

from matplotlib import pyplot as plt


def select_file_from(files: list) -> str:
    print('Select a file:')
    for i, f in enumerate(files): print(f'[{i}]: \t{f}')
    inp = input('Index: ').strip()

    try:
        idx = int(inp)
        if idx < 0 or idx >= len(files): raise IndexError(f'Specified index {idx} is out of range from 0 to exclusive {len(files)}')
        return idx
    except Exception as e:
        print(str(e))
        return select_file_from(files)


files = subprocess.check_output([ 'ls', 'data' ]).decode().strip().split('\n')

selected_file = select_file_from(files) if len(sys.argv) == 1 else sys.argv[1]

if len(sys.argv) > 2: raise ValueError('Too many args! Maximum argc is 2.')

with open(os.path.join('data', files[selected_file]), 'r') as data_file:
    lines = [line.strip() for line in data_file]

    xs = [float(x) for x in lines[0].split(', ')]
    ys = [float(y) for y in lines[1].split(', ')]


plt.plot(xs, ys)
plt.title(files[selected_file])
plt.show()