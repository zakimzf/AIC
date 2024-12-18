import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Define functions for navigating between windows
def open_window_2():
    window_1.destroy()
    create_window_2()

def open_window_3():
    window_2.destroy()
    create_window_3()

def open_window_4():
    window_3.destroy()
    create_window_4()

# Function to upload a file (but it doesn't affect the structure)
def upload_ontology_file():
    file_path = filedialog.askopenfilename(filetypes=[("OWX files", "*.owx"), ("XML files", "*.xml")])
    if file_path:
        print(f"File uploaded: {file_path}")
        messagebox.showinfo("File Upload", "Ontology file uploaded successfully.")
        # Display ontology structure after file upload
        create_window_1()
    else:
        messagebox.showerror("Error", "No file uploaded. Please upload a valid OWX or XML file.")

# Window 1: Ontology Structure
def create_window_1():
    global window_1
    window_1 = tk.Tk()
    window_1.title("Ontology Structure")

    label = tk.Label(
        window_1,
        text="Ontology Structure: AI Tutoring System for Algebra",
        font=("Arial", 16, "bold"),
    )
    label.pack(pady=10)

    structure = """
Ontology Structure:
1. Algebraic Topics
   - Linear Equations
   - Quadratic Equations
   - Polynomials
   - Inequalities
2. Algebraic Concepts
   - Variables
   - Coefficients
   - Expressions
   - Functions
3. Learning Resources
   - Video Tutorials
   - Interactive Exercises
   - PDF Worksheets
4. Problem Types
   - Solve Equations
   - Simplify Expressions
5. Assessment Methods
   - Multiple Choice Questions
   - Graphing Tasks
"""
    text = tk.Text(window_1, height=20, width=80)
    text.insert(tk.END, structure)
    text.configure(state="disabled")
    text.pack(pady=10)

    proceed_button = tk.Button(
        window_1, text="Proceed to Algebra", font=("Arial", 14), command=open_window_2
    )
    proceed_button.pack(pady=20)

    window_1.mainloop()

# Window 2: Algebra and Its Definition
def create_window_2():
    global window_2
    window_2 = tk.Tk()
    window_2.title("Algebra Overview")

    label = tk.Label(
        window_2, text="Algebra Overview", font=("Arial", 16, "bold")
    )
    label.pack(pady=10)

    definition = """
Algebra is a branch of mathematics that deals with symbols
and the rules for manipulating those symbols. It is used
to represent numbers and relationships between them.
"""
    text = tk.Text(window_2, height=10, width=60)
    text.insert(tk.END, definition)
    text.configure(state="disabled")
    text.pack(pady=10)

    proceed_button = tk.Button(
        window_2,
        text="Proceed to Algebra Concepts and Topics",
        font=("Arial", 14),
        command=open_window_3,
    )
    proceed_button.pack(pady=20)

    window_2.mainloop()

# Window 3: Algebra Concepts and Topics
def create_window_3():
    global window_3
    window_3 = tk.Tk()
    window_3.title("Algebra Concepts and Topics")

    label = tk.Label(
        window_3,
        text="Algebra Concepts and Topics",
        font=("Arial", 16, "bold"),
    )
    label.pack(pady=10)

    structure = """
Algebraic Concepts:
- Variables: Symbols representing unknown values.
- Coefficients: Numbers associated with variables.
- Expressions: Mathematical statements combining numbers and variables.
- Functions: Relationships between inputs and outputs.

Algebraic Topics:
- Linear Equations: Equations involving a straight-line graph.
- Quadratic Equations: Equations involving parabolic curves.
- Polynomials: Expressions involving powers and coefficients.
- Inequalities: Expressions showing less than or greater than relationships.
"""
    text = tk.Text(window_3, height=20, width=80)
    text.insert(tk.END, structure)
    text.configure(state="disabled")
    text.pack(pady=10)

    proceed_button = tk.Button(
        window_3,
        text="Proceed to Learning Resources and Problem Types",
        font=("Arial", 14),
        command=open_window_4,
    )
    proceed_button.pack(pady=20)

    window_3.mainloop()

# Window 4: Learning Resources, Access Methods, and Problems
def create_window_4():
    global window_4
    window_4 = tk.Tk()
    window_4.title("Learning Resources and Problem Types")

    label = tk.Label(
        window_4,
        text="Learning Resources and Problem Types",
        font=("Arial", 16, "bold"),
    )
    label.pack(pady=10)

    structure = """
Learning Resources:
- Video Tutorials: Interactive videos for topics like Linear Equations.
- Interactive Exercises: Hands-on exercises for Quadratic Equations.
- PDF Worksheets: Printable worksheets for Polynomials.

Access Methods:
- Explain Concept: Definitions and examples for better understanding.
- Belong to Topic: Associating resources with relevant algebra topics.

Problem Types:
- Solve Equations: Example: Solve 3x + 2 = 11.
- Simplify Expressions: Example: Simplify 2(x + 3) - 5.

Assessment Methods:
- Multiple Choice Questions: Evaluate understanding of concepts.
- Graphing Tasks: Graph equations to visualize relationships.
"""
    text = tk.Text(window_4, height=25, width=80)
    text.insert(tk.END, structure)
    text.configure(state="disabled")
    text.pack(pady=10)

    finish_button = tk.Button(
        window_4,
        text="Finish",
        font=("Arial", 14),
        command=window_4.destroy,
    )
    finish_button.pack(pady=20)

    window_4.mainloop()

# Initialize the main application window (for file upload)
upload_window = tk.Tk()
upload_window.title("Upload Ontology File")
upload_window.geometry("400x200")

# Create a button to upload ontology file
upload_button = tk.Button(upload_window, text="Upload OWL Ontology File", command=upload_ontology_file)
upload_button.pack(pady=50)

# Run the main loop of the first window (for file upload)
upload_window.mainloop()