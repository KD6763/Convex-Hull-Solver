# Convex Hull Solver

Solving Convex Hull problem using BruteForce and Graham Scan Algorithms. Language used is python 3.9

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Matplotlib.

```bash
pip install matplotlib
```

### Files Available
The folder contains 5 files in total
* Bruteforce.py - Python file to call Bruteforce implementation
* Graham Scan.py - Python file to call Graham Scan implementation
* Convexhelper.py - Python file containing all the helper functions for the above algorithms
* RandomGenerator.py - Python file to generate random points and storing into input file
* input.txt - Input file with all the points

### Imports
```python
import matplotlib.pyplot as plt
import time
import sys
import random
import Convexhelper as c
```

## Usage

### To run the Bruteforce Algorithm
```bash
python3 Bruteforce.py filename
```
Where the filename is the input file (input.txt)

### To run the Graham Scan Algorithm
```bash
python3 Graham Scan.py filename
```
Where the filename is the input file (input.txt)

### To run the Random points generator
```bash
python3 RandomGenerator.py number
```
Where the number is the number of random points to be generated

## Outputs
* The outputs will be stored in the files output_bf.txt and output_gs.txt respectively.
* Also shows the plot with the convex hull Drawn on it
* And the time taken to execute each Algorithm

