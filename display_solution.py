"""
A pretty-printer to display the solution.
"""


def main():
    def p(x, y, z): return (((x - 1) * 9) + (y - 1)) * 9 + z

    line = input()

    if line.strip() == "SAT":
        print("\n S O L U T I O N\n- - - - - - - - -")
        solution = input().split()

        for i in range(1, 10):
            for j in range(1, 10):
                for k in range(1, 10):
                    if str(p(i, j, k)) in solution:
                        print(f"{k} ", end='')
            print()

    else:
        print("\nGiven puzzle has no solutions.")


if __name__ == "__main__":
    main()
