#!/usr/bin/env python3
import sys


def main() -> None:
    """Generates sudoku.dimacs file."""

    def s(x: int, y: int, z: int) -> int:
        """Computes the s-value."""

        return 81 * (x - 1) + 9 * (y - 1) + z

    # Open puzzle and DIMACS files in the read and write modes respectively
    with open(sys.argv[1], "r") as puzzle, open("sudoku.dimacs", "w") as dimacs:
        # Read the puzzle and fill up the list for the preassigned entries
        row_num: int = 1
        col_num: int = 0
        preassigned: list[int] = []
        for _ in range(1, 10):
            line = puzzle.readline()
            digits = line.split()
            col_num = 0
            for digit in digits:
                col_num += 1
                if digit != "x":
                    preassigned.append(s(row_num, col_num, int(digit)))
            row_num += 1

        # A DIMACS file begins with a line containing 'p' followed by 'cnf', the number of
        # variables, and the number of clauses
        dimacs.write(f"p cnf 729 {8829 + len(preassigned)}\n")

        # Write the preassigned entries to the file
        for entry in preassigned:
            dimacs.write(f"{entry} 0\n")

        # There is at least one number in each entry
        for x in range(1, 10):
            for y in range(1, 10):
                for z in range(1, 10):
                    dimacs.write(f"{s(x, y, z)} ")
                dimacs.write("0\n")

        # Each number appears at most once in each row
        for y in range(1, 10):
            for z in range(1, 10):
                for x in range(1, 9):
                    for i in range(x + 1, 10):
                        dimacs.write(f"{-s(x, y, z)} {-s(i, y, z)} 0\n")

        # Each number appears at most once in each column
        for x in range(1, 10):
            for z in range(1, 10):
                for y in range(1, 9):
                    for i in range(y + 1, 10):
                        dimacs.write(f"{-s(x, y, z)} {-s(x, i, z)} 0\n")

        # Each number appears at most once in each 3x3 sub-grid
        for z in range(1, 10):
            for i in range(0, 3):
                for j in range(0, 3):
                    for x in range(1, 4):
                        for y in range(1, 4):
                            for k in range(y + 1, 4):
                                dimacs.write(
                                    f"{-s(3 * i + x, 3 * j + y, z)} "
                                    f"{-s(3 * i + x, 3 * j + k, z)} 0\n"
                                )

        # Each number appears at most once in each 3x3 subgrid
        for z in range(1, 10):
            for i in range(0, 3):
                for j in range(0, 3):
                    for x in range(1, 4):
                        for y in range(1, 4):
                            for k in range(x + 1, 4):
                                for l in range(1, 4):
                                    dimacs.write(
                                        f"{-s(3 * i + x, 3 * j + y, z)} "
                                        f"{-s(3 * i + k, 3 * j + l, z)} 0\n"
                                    )


if __name__ == "__main__":
    main()
