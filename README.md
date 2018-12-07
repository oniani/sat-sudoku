# MiniSat sudoku solver

This is the implementation of the minisat sudoku solver based on the [paper](paper.pdf) by Inês Lynce and Jöel Ouaknine.

Sudoku is modeled as the SAT problem. The idea is to formulate a sudoku puzzle as a SAT formula if the puzzle has a solution. Then we use [MiniSat](http://minisat.se/) solver to find the solution.

[MiniSat](http://minisat.se/) is a program that solves the satisfiability problem: given a formula, it either returns an assignment that makes it true, or says that no such assignment exists. It uses a restricted form of propositional formula called CNF (Conjunctive Normal Form). CNF consists of a set of clauses, each of which is a set of literals. A literal is a variable or its negation. Each clause is interpreted as the disjunction of its literals, and the formula as a whole is interpreted as the conjunction of the clauses.

For the in-depth explanation of how the sudoku solver works, see the [paper](paper.pdf).

## Setup

### macOS
```bash
$ brew install minisat
$ git clone https://github.com/oniani/minisat-sudoku.git
$ cd minisat-sudoku
$ ./solve PATH_TO_THE_PUZZLE
```

### Linux
```bash
$ sudo apt-get update
$ sudo apt-get install minisat
$ git clone https://github.com/oniani/minisat-sudoku.git
$ cd minisat-sudoku
$ ./solve PATH_TO_THE_PUZZLE
```

### Windows
Follow this [guide](http://web.cecs.pdx.edu/~hook/logicw11/Assignments/MinisatOnWindows.html).

There are 9 sample puzzles available under directory called `puzzles`.

To solve the first puzzle, simply run `./solve puzzles/sudoku1.puzzle`.

## References
* [Inês Lynce and Jöel Ouaknine, Sudoku as a SAT Problem](paper.pdf)
* [MiniSat](http://minisat.se/)
* [Sudoku](https://en.wikipedia.org/wiki/Sudoku)

## License
[MIT](https://github.com/oniani/minisat-sudoku/blob/master/LICENSE)
