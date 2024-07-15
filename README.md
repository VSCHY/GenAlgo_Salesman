# GenAlgo_Salesman
**Solving the Traveling Salesman Problem using a Genetic Algorithm**

<p align="center">
  <img src="docs/image.png" alt="GeneticAlgo" width="500" />
</p>

Welcome to the pedagogical project on solving the Traveling Salesman Problem (TSP) using a Genetic Algorithm (GA). This repository aims to provide a clear and educational implementation of a GA to tackle the TSP, designed for students and educators.

## Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Genetic Algorithm Overview](#genetic-algorithm-overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Traveling Salesman Problem (TSP) is a classic and notoriously challenging optimization problem that has puzzled mathematicians and computer scientists for decades. Despite extensive research, no polynomial-time solution exists, making it an **NP-hard problem**. 
**NP-hard problem** refers to a class of problems that are some of the most challenging computational puzzles to solve. In computational complexity theory, NP-Hardness is used to classify problems that are, in a sense, as hard as the hardest problems in NP (nondeterministic polynomial time). Essentially, if a problem is NP-Hard, it means that its solution can be verified quickly, but there is no known efficient method to locate a solution. This categorization places NP-Hard problems at the pinnacle of computational complexity, making them crucial to understand within the realm of AI algorithms and problem-solving.


As a result, brute force methods, which involve evaluating all possible permutations, quickly become impractical for even moderately sized instances. However, Genetic Algorithms (GAs) offer a smart and elegant approach to exploring possible solutions. Inspired by the principles of natural selection and evolution, GAs simulate the process of natural evolution to iteratively improve solutions, balancing exploration and exploitation in the search space. This project leverages the power of GAs to provide an educational and practical implementation for solving the TSP, demonstrating how nature-inspired algorithms can effectively tackle complex computational problems.

## Problem Statement

In the TSP, a salesman is required to visit a set of cities exactly once and return to the starting city, with the objective of minimizing the total travel distance. The TSP is known for its computational complexity and is an NP-hard problem.

## Genetic Algorithm Overview

A Genetic Algorithm is an optimization technique inspired by the process of natural selection. It operates through a cycle of selection, crossover, and mutation to evolve solutions to a given problem. The key steps in our GA for the TSP are:

1. **Initialization**: Generate an initial population of possible routes.
2. **Selection**: Select routes from the current population based on their fitness (shorter routes are preferred).
3. **Crossover**: Combine pairs of routes to produce offspring.
4. **Mutation**: Introduce random changes to offspring routes to maintain genetic diversity.
5. **Replacement**: Form a new population by replacing some of the old routes with new ones.

In our case, part of the next population is created based on crossover (without aggregated mutation) and one other part is created from mutation of selected individuals (based on similar logic as selected parents for crossover).

## Selection Options
The selection process is a crucial part of a Genetic Algorithm as it determines which individuals (routes) will be chosen to reproduce and form the next generation. The available selection options in this project are:

- **Uniform**: Every individual has an equal chance of being selected.
- **Elitist**: Only the top-performing individuals are selected to reproduce.
- **Lottery**: Individuals are selected based on a weighted probability, giving higher chances to better performers.
- **Tournament**: Groups of individuals compete against each other, and the best from each group is selected. It is like elitist logic but applied on subsample.
- **Random**: Individuals are selected completely at random, regardless of their performance.


These options provide flexibility in how the genetic algorithm explores and exploits the search space, helping to balance the diversity of solutions and the convergence towards optimal solutions.


## Project Structure

```plaintext
├── inputs/
│   ├── TSP1/                # Folder with input data for first problem
│   ├── TSP2/                # Folder with input data for second problem
├── LICENSE
├── main.ipynb               # Main Jupyter notebook for running the project
├── README.md
├── src/
│   ├── functions_basic.py   # Basic functions
│   ├── functions_pop.py     # Functions at population level
│   ├── genetic.py           # Class with genetic algorithm
│   ├── __init__.py
│   ├── problem.py           # Read inputs
```

## Installation

To get started, clone this repository and install the required dependencies:

```sh
git clone git@github.com:VSCHY/GenAlgo_Salesman.git
cd GenAlgo_Salesman
```

## Usage

Run the main Jupyter notebook to see the Genetic Algorithm in action:

This notebook will demonstrate how the GA solves TSP instances using the sample datasets provided in the `inputs` directory.


## Contributing

We welcome contributions from the community! If you have suggestions for improvements or new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the terms of the [GNU General Public License v3.0](LICENSE).
