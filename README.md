# Efficient Page Replacement Algorithm Simulator

## Overview
The **Efficient Page Replacement Algorithm Simulator** is a graphical tool designed to help users test and compare different page replacement algorithms, including:
- FIFO (First-In-First-Out)
- LRU (Least Recently Used)
- Optimal (OPT)
- Clock Algorithm

The simulator provides visualizations and performance metrics to analyze the efficiency of each algorithm in handling page faults.

## Features
- **User-Friendly GUI**: Built using Tkinter for easy interaction.
- **Multiple Algorithms**: Supports FIFO, LRU, Optimal, and Clock page replacement techniques.
- **Real-Time Visualization**: Uses Matplotlib to display page replacement operations step by step.
- **Performance Analysis**: Displays the number of page faults for each algorithm.
- **Custom Input**: Users can enter their own reference string and frame size.

## Installation
To use this simulator, follow these steps:

### Prerequisites
Ensure you have Python installed (preferably Python 3.7+). Also, install the required dependencies:
```bash
pip install tkinter matplotlib
```

### Clone the Repository
```bash
git clone https://github.com/tripathi-22/Efficient-Page-Replacement-Simulator.git
cd Efficient-Page-Replacement-Simulator
```

## Usage
Run the script to start the simulator:
```bash
python main.py
```

### Steps to Use
1. Enter the number of frames and a reference string.
2. Select a page replacement algorithm.
3. Click "Run Simulation" to visualize the process.
4. View results including page faults and step-by-step execution.

## Example
Sample reference string: `7, 0, 1, 2, 0, 3, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1`
Frame size: `3`

The simulator will display step-by-step page replacements and compute the total number of page faults.

## Contribution
Feel free to contribute by submitting pull requests or reporting issues. To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Added new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## Contact
For questions or suggestions, contact:
- **Sameer Tripathi**
- **Email: tripathisam2204@gmail.com**
- **GitHub: [tripathi-22](https://github.com/tripathi-22)**

