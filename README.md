#  Medusa
_A python library of commonly used, parallel algorithms_

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Philosophy](#philosophy)
- [Algorithms](#algorithms)
  - [Sorting Algorithms](#sorting)
  - [Matrix Operations](#matrix)
  - [Graph Algorithms](#graphs)
- [Tests](#tests)

### <a name="overview"></a>Overview
Medusa is a Python library of common, parallelized algorithms is proposed in order to meet the perceived need of professionals in data-heavy fields for parallel solutions without explicit parallel knowledge and understanding.The collection of algorithms is implemented in Python 3 and requires the multiprocessing package, as well as NumPy and networkx for certain modules. The multiprocessing package allows for parallel implementation over both shared and distributed memory, though Medusa is designed to be run on a distributed memory system.

### <a name="philosophy"></a>Philosophy
Medusa is intended for use by scientists and programmers in technical and computational fields, but who may not have a programming background. Medusa is developed in Python using the multiprocessing module in order to parallelize code, which results in slower runtimes compared to other languages, such as C++. Naturally, we come to emphasize ease of use and abstraction over raw speed. Runtime efficiency is, of course, an important trait in parallel code, but is not a priority over simplicity.

### <a name="installation"></a>Installation
#### Using conda to create a virtual environment (recommended)
The recommended method of setting up the required Python environment and dependencies 
is to use the [conda](https://conda.io/docs/) dependency manager:
```
$ conda create -n py36 python=3.6.1           # Create a python3.6 virtual environment
$ source activate py36                        # Activate the virtual environment
$ conda install --file requirements.txt       # Install dependencies
```

#### Installing from source
```
$ git clone https://github.com/Akards/Medusa.git     # Clone the repo
$ cd Medusa                                          # Switch to the MICA root directory
$ python setup.py install                            # Install MICA from source
```


### <a name="usage"></a>Usage

### <a name="algorithms"></a>Algorithms
Below, you can find the current classes of algorithms in Medusa. Within each subsection, all currently implemented algorithms are listed. Any further documentation can be found on the README files found inside each module.
#### <b name="sorting"></b>Sorting Algorithms
Any sorting algorithms are included in the module `Medusa/sort/`.
- Merge Sort
- Bitonic Sort
- Paradis

#### <b name="matrix"></b>Matrix Operations
Any matrix operations, or linear algebra related algorithms are included in `/Medusa/matrix/`. Matrix operations are implemented using NumPy arrays in order to improve runtime efficiency.
- Multiplication
- Addition

#### <b name="graphs"></b>Graph Algorithms
Any algorithms related to graphs are included in `/Medusa/graphs/`. These are implemented taking into account the use of [networkx](https://networkx.github.io/).
- Breadth-first search
- Boruvka's Algorithm

### <a name="tests"></a>Testing
Unit testing for Medusa is implemented using the [pytest](https://docs.pytest.org/en/latest/) package. In order to run all of the tests from the project's root, simply call:
`python -m pytest`
