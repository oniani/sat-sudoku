# Minisat sudoku solver

This is the implementation of the minisat sudoku solver based on the [paper](https://pdfs.semanticscholar.org/535d/06391275618a7b913d1c98a1353286db8d74.pdf) by Inês Lynce and Jöel Ouaknine.

Sudoku is modeled as the SAT problem. The idea is to formulate a sudoku puzzle as a SAT formula if the puzzle has a solution. Then we use the [minisat](http://minisat.se/) program to find the solution.

A minisat solver is a program that solves the satisfiability problem: given a formula, it either returns an assignment that makes it true, or says that no such assignment exists. SAT solvers typically use a restricted form of propositional formula called CNF (conjunctive normal form). CNF consists of a set of clauses, each of which is a set of literals. A literal is a variable or its negation. Each clause is interpreted as the disjunction (OR) of its literals, and the formula as a whole is interpreted as the conjunction (AND) of the clauses.


## Representation
To model sudoku as a SAT problem, we represent it as a grid of digits where the unknown cells
are called the 'x cells'.

Here are some of the examples of the sudoku problems.

```
    x 7 x x x x 3 x 1    x 7 x 5 x 4 x 2 x    x 6 x x x 7 5 2 x
    x 3 x 5 7 2 x x 6    x x x x x x 7 x x    x x x 9 x x 6 x x
    4 6 x x x x 5 x x    6 x 4 x x x 1 x 9    1 x x x x x 8 x 7
    x 8 1 x x x x x x    x x x 3 x 9 x x x    x x x 3 x x x 1 2
    x x x 3 x 5 x x x    x 9 2 x x x 5 8 x    x x 3 5 x 1 4 x x
    x x x x x x 4 6 x    x x x 2 x 5 x x x    4 2 x x x 8 x x x
    x x 6 x x x x 8 9    4 x 1 x x x 6 x 8    5 x 8 x x x x x 6
    8 x x 1 4 6 x 5 x    x x 6 x x x x x x    x x 7 x x 9 x x x
    2 x 7 x x x x 3 x    x 3 x 8 x 6 x 9 x    x 9 6 4 x x x 8 x
```


## Running the solver

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
Follow the [link](http://web.cecs.pdx.edu/~hook/logicw11/Assignments/MinisatOnWindows.html).

# License
[MIT](https://github.com/oniani/minisat-sudoku/blob/master/LICENSE)
