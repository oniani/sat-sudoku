# SAT sudoku solver
This is the implementation of the SAT sudoku solver based on the paper by Inês Lynce and Jöel Ouaknine called *Sudoku as a SAT Problem*.

Sudoku is modeled as the SAT problem. The idea is to formulate a sudoku puzzle as a SAT formula if the puzzle has a solution. Then we use the SAT program to find the solution.

SAT is a program that solves the satisfiability problem: given a formula, it either returns an assignment that makes it true, or says that no such assignment exists. It uses a restricted form of propositional formula called CNF (Conjunctive Normal Form). CNF consists of a set of clauses, each of which is a set of literals. A literal is a variable or its negation. Each clause is interpreted as the disjunction of its literals, and the formula as a whole is interpreted as the conjunction of the clauses.

This implementation uses [MiniSat](http://minisat.se/).

For the in-depth explanation of how the sudoku solver works, see the [paper](paper.pdf).

## Setup

### macOS
```bash
$ brew install minisat
$ git clone https://github.com/oniani/minisat-sudoku.git
$ cd minisat-sudoku
$ ./solve A_PATH_TO_THE_PUZZLE
```

### Linux
```bash
$ sudo apt-get update
$ sudo apt-get install minisat
$ git clone https://github.com/oniani/minisat-sudoku.git
$ cd minisat-sudoku
$ ./solve A_PATH_TO_THE_PUZZLE
```

## Windows
Follow this [guide](http://web.cecs.pdx.edu/~hook/logicw11/Assignments/MinisatOnWindows.html).

---
There are 9 sample sudoku puzzles available under directory called `puzzles`.  
To solve the first puzzle, simply run `./solve puzzles/sudoku1.puzzle`.

## References
* [Inês Lynce and Jöel Ouaknine, Sudoku as a SAT Problem](paper.pdf)
* [MiniSat](http://minisat.se/)
* [Sudoku](https://en.wikipedia.org/wiki/Sudoku)

## License
[GNU General Public License v3.0](LICENSE)
