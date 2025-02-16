def simulate_fifo(page_references, num_frames):
    """
    Simulate the FIFO (First-In, First-Out) page replacement algorithm.
    
    Parameters:
        page_references (list of int): The sequence of page requests.
        num_frames (int): Number of available memory frames.
    
    Returns:
        simulation_steps (list of dict): A record of each simulation step.
          Each dict contains:
            - 'step': Simulation step number.
            - 'page': Current page being processed.
            - 'frames': A copy of the current frames list.
            - 'fault': True if a page fault occurred.
            - 'fault_count': Cumulative page faults so far.
    """
    frames = []
    simulation_steps = []
    page_faults = 0

    for i, page in enumerate(page_references):
        fault = False
        # Check if the page is already in memory
        if page not in frames:
            page_faults += 1
            fault = True
            # If there is room, simply add the page; otherwise, replace the oldest page
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)  # Remove the oldest page (FIFO)
                frames.append(page)
        # Record the state for this simulation step
        simulation_steps.append({
            "step": i + 1,
            "page": page,
            "frames": frames.copy(),
            "fault": fault,
            "fault_count": page_faults
        })

    return simulation_steps

if __name__ == "__main__":
    # Example input
    page_references = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    num_frames = 3

    # Run FIFO simulation
    simulation_steps = simulate_fifo(page_references, num_frames)
    
    # Print the simulation steps to the console
    for step in simulation_steps:
        print(f"Step {step['step']}: Page {step['page']} - ", end="")
        if step['fault']:
            print("Page Fault! ", end="")
        else:
            print("No Fault. ", end="")
        print(f"Frames: {step['frames']} | Cumulative Faults: {step['fault_count']}")
