import tkinter as tk
from tkinter import messagebox

# This function runs when the user clicks the button
def calculate_average():
    try:
        # Get the text typed into each Entry box
        # .get() reads whatever the user typed
        s1 = float(entry1.get())   # Convert score 1 to a number
        s2 = float(entry2.get())   # Convert score 2 to a number
        s3 = float(entry3.get())   # Convert score 3 to a number

        # Add the three scores and divide by 3 to get the average
        avg = (s1 + s2 + s3) / 3

        # Show the average in the label
        # :.2f means "round to 2 decimal places"
        result_label.config(text=f"Average: {avg:.2f}")

    except ValueError:
        # This happens if the user types something that isn't a number
        messagebox.showerror("Invalid Input", "Please enter numbers only.")
        result_label.config(text="Average: ---")

# Create the main window
root = tk.Tk()
root.title("Test Score Averager")   # Title at the top of the window
root.geometry("300x220")            # Set the window size

# Label + Entry for Score 1
tk.Label(root, text="Enter Score 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

# Label + Entry for Score 2
tk.Label(root, text="Enter Score 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Label + Entry for Score 3
tk.Label(root, text="Enter Score 3:").pack()
entry3 = tk.Entry(root)
entry3.pack()

# Button that