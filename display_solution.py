#!/usr/bin/env python3
def main() -> None:
    """Displays the solution to a puzzle."""

    def p(x: int, y: int, z: int) -> int:
        """Computes the p-value."""

        return (((x - 1) * 9) + (y - 1)) * 9 + z

    line: str = input()

    if line.strip() == "SAT":
        print(" S O L U T I O N\n- - - - - - - - -")

        solution: list[str] = input().split()

        for i in range(1, 10):
            for j in range(1, 10):
                for k in range(1, 10):
                    if str(p(i, j, k)) in solution:
                        print(k, end=" ")
            print()

    else:
        print("\nGiven puzzle has no solutions")


if __name__ == "__main__":
    main()
