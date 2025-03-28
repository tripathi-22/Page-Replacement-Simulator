# Page Replacement Algorithm Simulator

A GUI application to simulate and visualize different page replacement algorithms using Python and Tkinter.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Algorithms Implemented](#algorithms-implemented)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Project Description
This application provides a graphical interface to simulate and analyze different page replacement algorithms used in operating systems' memory management. Users can input custom page sequences, select algorithms, and visualize the results through tables and graphs.

## Features
- Interactive GUI with input validation
- Support for four page replacement algorithms:
  - FIFO (First-In First-Out)
  - LRU (Least Recently Used)
  - Optimal
  - Clock (Second Chance)
- Real-time results display with color-coded page faults
- Performance graph visualization
- Algorithm comparison chart
- Frame state visualization for each step
- File I/O operations (save/load results)
- Tooltips for better usability

## Algorithms Implemented
1. **FIFO**: Removes the oldest page in memory
2. **LRU**: Removes the least recently used page
3. **Optimal**: Removes the page that won't be used for the longest time (future-aware)
4. **Clock**: Uses a circular buffer with reference bits

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/tripathi-22/page-replacement-simulator.git

2. Install required dependencies:
pip install matplotlib

## Usage

1. Run the application:
python page_replacement.py

2. Input parameters:
a. Page Sequence (comma-separated numbers)
b. Number of frames
c. Select algorithm from dropdown

3. Use buttons to:
a. Run simulation
b. Compare all algorithms
c. Show performance graph
d. Load/Save sequences
e. Clear inputs

## Examples

Sample Input:
Page Sequence: 1,2,3,4,1,2,5,1,2,3,4,5
Number of Frames: 3
Selected Algorithm: LRU

Expected Output:
Step-by-step table of page replacements

Page fault statistics

Cumulative fault graph

Visual representation of frame states

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## Acknowledgements

1. Python Tkinter for GUI development
2. Matplotlib for graph visualization
3. Standard page replacement algorithm references
