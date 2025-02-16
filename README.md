# Effective Simulator for Page Replacement

First-In, First-Out (FIFO) and LRU (Least Recently Used) are two popular page replacement algorithms that are illustrated via the interactive Python application Efficient Page Replacement Simulator. In addition to displaying a detailed simulation log and an embedded Matplotlib graph that illustrates the cumulative page faults over time, the program employs a Tkinter-based GUI to gather user input.

## Detailed Operation

### Engine for Simulation

There are two features in the simulation engine:

The goal of **simulate_fifo(page_references, num_frames)** is to implement the FIFO algorithm.
  **How It Operates:**
    The list of page requests is iterated over.
    - Keeps track of the current pages in memory in a list (`frames`).
    For every page:
      Nothing changes if the page is already in memory.
      A page fault happens if the page is not in memory.
        If space permits, the page is merely included.
        The oldest page (first in the list) is deleted and a new page is added if memory is full.
    Details (current page, frame condition, fault occurrence, and cumulative faults) are recorded for every step.

The function **simulate_lru(page_references, num_frames)** - **Goal:** carries out the LRU algorithm.
  **How It Operates:**
    The page reference list is iterated over.
    Preserves:
      Current pages are stored in a `frames` list.
      A list called `usage_order` is used to keep track of how recently each page has been used.
    For every page:
      If the page exists, the `usage_order` is updated to reflect its most recent usage.
      If the page is missing, something goes wrong:
        The page is added if there is room.
        The first page in `usage_order`, which is the least recently used, is deleted if memory is full, and the new A new page has been added.
    Every simulation step is recorded in a manner consistent with the FIFO function.

### User Interface Graphics (GUI)

The GUI is divided into three primary components and was constructed with Tkinter:

1. **Input Section:** - **Page References:** A text field where a list of page numbers separated by commas can be entered.
   - **Number of Frames:** A field to specify the number of available memory frames.
   **Selection of Algorithm:** Radio buttons to select between LRU and FIFO.

2. **Simulation Log:** - Detailed information about every simulation phase is displayed in a text widget.
   - It displays the current page, frame condition, number of cumulative faults, and whether a fault occurred.

3. **Visualization Section:** - A graph with the following features is displayed via an embedded Matplotlib plot: **X-Axis:** Simulation steps.
     Cumulative page faults on the Y-axis.
   As the simulation progresses, this real-time graph is updated, enabling people to examine the algorithm's performance visually.

### Using the Simulator

1. Make a copy of the repository:
   ```bash cd page-replacement-simulator git clone https://github.com/yourusername/page-replacement-simulator.git
