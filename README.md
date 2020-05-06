#  Medusa
_A python library of common, parallel algorithms_

## Table of Contents
- [Philosophy](#philosophy)
- [Overview](#overview)
- [Algorithms](#algorithms)
  - [Sorting Algorithms](#sorting)
  - [Matrix Operations](#matrix)
  - [Graph Algorithms](#graphs)
  
  
### <a name="philosophy"></a>Philosophy
Medusa is intended for use by scientists and programmers in technical and computational fields, but who may not have a programming background. Medusa is developed in Python using the multiprocessing module in order to parallelize code, which results in slower runtimes compared to other languages, such as C++. Naturally, we come to emphasize ease of use and abstraction over raw speed. Runtime efficiency is, of course, an important trait in parallel code, but is not a priority over simplicity.

### <a name="overview"></a>Overview

### <a name="algorithms"></a>Algorithms
Below, you can find the current classes of algorithms in Medusa.
#### <b name="sorting"></b>Sorting Algorithms
Any sorting algorithms are included in the module `Medusa/sort/`.

Currently included:
- Merge Sort
- Bitonic Sort
- Paradis

#### <b name="matrix"></b>Matrix Operations
Any matrix operations, or linear algebra related algorithms are included in `/Medusa/matrix/`. Matrix operations are implemented using NumPy arrays in order to improve runtime efficiency.

Currently included:
- Multiplication
- Addition

#### <b name="graphs"></b>Graph Algorithms
Any algorithms related to graphs are included in `/Medusa/graphs/`. These are implemented taking into account the use of [networkx](https://networkx.github.io/).

Currently included:
- Breadth-first search
- Boruvka's Algorithm
