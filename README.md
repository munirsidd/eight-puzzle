# Eight Puzzle Solver

## Introduction

The Eight Puzzle Solver is a Python project that employs various state-space search algorithms to solve the Eight Puzzle, a classic puzzle involving a 3x3 grid with eight numbered tiles and one blank space. The goal is to rearrange the tiles from an initial configuration to a specified target state. This project includes multiple search methods and heuristic functions to efficiently find solutions for Eight Puzzles.

## Project Components

### Search Algorithms

The project implements the following state-space search algorithms:

1. **Random Search (Algorithm: 'random')**:
   - An uninformed search that randomly selects moves.
   - Suitable for baseline comparisons.

2. **Breadth-First Search (Algorithm: 'BFS')**:
   - An uninformed search that explores all nodes at a given depth before moving to the next level.
   - Suitable for finding optimal solutions.

3. **Depth-First Search (Algorithm: 'DFS')**:
   - An uninformed search that explores as far as possible along each branch before backtracking.
   - May not find optimal solutions.

4. **Greedy Best-First Search (Algorithm: 'Greedy')**:
   - An informed search that uses heuristic functions to prioritize states based on estimated cost.
   - Utilizes heuristic functions (h0, h1, and h2) for estimation.

5. **A\* Search (Algorithm: 'A\*')**:
   - An informed search that combines the cost to reach a state and an estimated cost to the goal.
   - Utilizes heuristic functions (h0, h1, and h2) for estimation.

### Heuristic Functions

The project includes three heuristic functions to estimate the cost to reach the goal state:

#### Heuristic Function h0 (Zero Heuristic)
- Always returns 0.
- Provides no additional information about the number of moves needed.

#### Heuristic Function h1 (Misplaced Tiles Heuristic)
- Estimates the number of additional moves by counting misplaced tiles (excluding the blank tile).
- Provides a basic estimation based on the number of tiles out of place.

#### Heuristic Function h2 (Manhattan Distance Heuristic)
- Estimates the number of additional moves by calculating the Manhattan distance of each misplaced tile from its goal position.
- Considers both row-wise and column-wise distances for all misplaced tiles (excluding the blank tile).
- Offers a more accurate estimation of the cost.

## Getting Started

To use the Eight Puzzle Solver, run the `eight_puzzle.py` script and follow these steps:

1. Ensure you have all the necessary files (`board.py`, `searcher.py`, `state.py`, `timer.py`, and `eight_puzzle.py`) in the same directory.

2. Choose an Eight Puzzle configuration (represented by a digit string), a search algorithm and parameter, and run: 

   ```python
   eight_puzzle(board_config, algorithm, param)
   ```
   
   Alternatively, create a text file containing multiple board configurations, or use one of the files provided in the `sample_puzzles` directory, and run:

   ```python
   process_file(filename, algorithm, param)
   ```  

   - Replace board_config with an initial board configuration, e.g. '312065748'.
   - Replace algorithm with one the supported algorithms: 'random', 'BFS', 'DFS', 'Greedy', or 'A*'.
   - For the 'random', 'BFS' and 'DFS' algorithms, replace param with a depth limit (-1 if you don't want one). 
   - For the 'Greedy' and 'A*' algorithms, replace param with one of the heuristic functions: h0, h1, or h2.

4. Observe the solver in action!

## Enjoy Solving Eight Puzzles!