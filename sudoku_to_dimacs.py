"""
--------------------
Author: David Oniani
Date: 12/05/2018
License: MIT
--------------------

An implementation of the minisat sudoku solver
according to https://pdfs.semanticscholar.org/535d/06391275618a7b913d1c98a1353286db8d74.pdf

For more information, see https://en.wikipedia.org/wiki/Sudoku
"""


import sys


def main():
    puzzle = open(sys.argv[1], 'r')
    dimacs = open('sudoku.dimacs', 'w', newline='')

    def s(x, y, z): return 81 * (x - 1) + 9 * (y - 1) + z

    preassigned_entries = []
    preassigned_entries_count = 0

    row_number = 1
    column_number = 0

    for i in range(1, 10):
        line = puzzle.readline()
        digits = line.split()
        column_number = 0
        for digit in digits:
            column_number += 1
            if digit != 'x':
                preassigned_entries.append(s(row_number, column_number, int(digit)))
                preassigned_entries_count += 1
        row_number += 1

    dimacs.write(f"p cnf 729 {8829 + preassigned_entries_count}\n")

    for entry in preassigned_entries:
        dimacs.write(f"{entry} 0\n")

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                dimacs.write(f"{s(i, j, k)} ")
            dimacs.write("0\n")

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 9):
                for l in range(k + 1, 10):
                    dimacs.write(f"{-s(k, i, j)} {-s(l, i, j)} 0\n")

    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 9):
                for l in range(k + 1, 10):
                    dimacs.write(f"{-s(i, k, j)} ")
                    dimacs.write(f"{-s(i, l, j)} 0\n")

    for i in range(1, 10):
        for j in range(0, 3):
            for k in range(0, 3):
                for l in range(1, 4):
                    for m in range(1, 4):
                        for n in range(m + 1, 4):
                            dimacs.write(f"{-s(3 * j + l, 3 * k + m, i)} ")
                            dimacs.write(f"{-s(3 * j + l, 3 * k + n, i)} 0\n")

    for i in range(1, 10):
        for j in range(0, 3):
            for k in range(0, 3):
                for l in range(1, 4):
                    for m in range(1, 4):
                        for n in range(l + 1, 4):
                            for o in range(1, 4):
                                dimacs.write(f"{-s(3 * j + l, 3 * k + m, i)} ")
                                dimacs.write(f"{-s(3 * j + n, 3 * k + o, i)} 0\n")

    puzzle.close()
    dimacs.close()


if __name__ == "__main__":
    main()
