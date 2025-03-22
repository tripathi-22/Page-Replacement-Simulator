import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")  # Use TkAgg backend for embedding in Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# ==============================
# Simulation Engine Module
# ==============================

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



# ==============================
# GUI & Visualization Module
# ==============================

class PageReplacementSimulatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Efficient Page Replacement Algorithm Simulator")
        self.geometry("1000x700")
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange all GUI components."""
        # ------------------------------
        # Input Frame
        # ------------------------------
        input_frame = ttk.LabelFrame(self, text="Simulation Parameters")
        input_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        # Page References Input
        ttk.Label(input_frame, text="Page References (comma-separated):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.page_entry = ttk.Entry(input_frame, width=50)
        self.page_entry.grid(row=0, column=1, padx=5, pady=5)
        # Insert an example value
        self.page_entry.insert(0, "7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2")

        # Number of Frames Input
        ttk.Label(input_frame, text="Number of Frames:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.frame_entry = ttk.Entry(input_frame, width=10)
        self.frame_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        self.frame_entry.insert(0, "3")

        # Algorithm Selection (Radio Buttons)
        ttk.Label(input_frame, text="Algorithm:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.algo_var = tk.StringVar(value="FIFO")
        algo_frame = ttk.Frame(input_frame)
        algo_frame.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
        ttk.Radiobutton(algo_frame, text="FIFO", variable=self.algo_var, value="FIFO").pack(side=tk.LEFT)
        ttk.Radiobutton(algo_frame, text="LRU", variable=self.algo_var, value="LRU").pack(side=tk.LEFT)

        # Control Buttons: Run and Reset
        run_button = ttk.Button(input_frame, text="Run Simulation", command=self.run_simulation)
        run_button.grid(row=3, column=0, padx=5, pady=10)
        reset_button = ttk.Button(input_frame, text="Reset", command=self.reset_simulation)
        reset_button.grid(row=3, column=1, padx=5, pady=10, sticky=tk.W)

        # ------------------------------
        # Output Frame (Text Widget)
        # ------------------------------
        output_frame = ttk.LabelFrame(self, text="Simulation Details")
        output_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.text_output = tk.Text(output_frame, height=15)
        self.text_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=self.text_output.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_output.config(yscrollcommand=scrollbar.set)

        # ------------------------------
        # Plot Frame (Matplotlib Graph)
        # ------------------------------
        plot_frame = ttk.LabelFrame(self, text="Performance Graph")
        plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=plot_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def run_simulation(self):
        """Read inputs, run the selected simulation, and update the outputs."""
        # Validate and parse inputs
        try:
            page_ref_input = self.page_entry.get()
            # Convert comma-separated string into a list of integers
            page_references = [int(x.strip()) for x in page_ref_input.split(',') if x.strip() != '']
            num_frames = int(self.frame_entry.get())
            algorithm = self.algo_var.get()

            if not page_references:
                raise ValueError("Page references are empty.")
            if num_frames <= 0:
                raise ValueError("Number of frames must be positive.")
        except Exception as e:
            messagebox.showerror("Input Error", f"Invalid input: {str(e)}")
            return

        # Run the appropriate simulation
        if algorithm == "FIFO":
            simulation_steps = simulate_fifo(page_references, num_frames)
        elif algorithm == "LRU":
            simulation_steps = simulate_lru(page_references, num_frames)
        else:
            messagebox.showerror("Algorithm Error", "Unsupported algorithm selected.")
            return

        # Update the text widget with simulation details
        self.display_simulation(simulation_steps)
        # Update the embedded plot with cumulative page faults
        self.update_plot(simulation_steps)

    def display_simulation(self, simulation_steps):
        """Display the simulation steps in the text output widget."""
        self.text_output.delete("1.0", tk.END)
        for step in simulation_steps:
            step_text = f"Step {step['step']}: Page {step['page']} - "
            if step['fault']:
                step_text += "Page Fault! "
            else:
                step_text += "No Fault. "
            step_text += f"Frames: {step['frames']} | Cumulative Faults: {step['fault_count']}\n"
            self.text_output.insert(tk.END, step_text)

    def update_plot(self, simulation_steps):
        """Update the matplotlib plot with cumulative page faults over the simulation steps."""
        # Extract data for plotting
        steps = [step['step'] for step in simulation_steps]
        faults = [step['fault_count'] for step in simulation_steps]

        # Clear the previous figure and create a new subplot
        self.figure.clf()
        ax = self.figure.add_subplot(111)
        ax.plot(steps, faults, marker='o', linestyle='-')
        ax.set_title("Cumulative Page Faults Over Time")
        ax.set_xlabel("Step")
        ax.set_ylabel("Cumulative Page Faults")
        ax.grid(True)
        self.canvas.draw()

    def reset_simulation(self):
        """Reset all input fields, text output, and the plot."""
        self.page_entry.delete(0, tk.END)
        self.frame_entry.delete(0, tk.END)
        self.text_output.delete("1.0", tk.END)
        self.figure.clf()
        self.canvas.draw()

# ==============================
# Main Execution
# ==============================

if __name__ == "__main__":
    app = PageReplacementSimulatorGUI()
    app.mainloop()
