#!/usr/bin/env python3
# encoding: UTF-8

"""A pretty-printer to display the solution."""

__author__ = "David Oniani"
__email__ = "onianidavid@gmail.com"
__license__ = "GPLv3"


def main() -> None:
    def p(x, y, z):
        return (((x - 1) * 9) + (y - 1)) * 9 + z

    line = input()

    if line.strip() == "SAT":
        print("\n S O L U T I O N\n- - - - - - - - -")
        solution = input().split()

        for i in range(1, 10):
            for j in range(1, 10):
                for k in range(1, 10):
                    if str(p(i, j, k)) in solution:
                        print(k, end=" ")
            print()

    else:
        print("\nGiven puzzle has no solutions.")


if __name__ == "__main__":
    main()
