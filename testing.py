import tkinter as tk

# Create the main window
windows = tk.Tk()

# Create a Frame with padding
frame = tk.Frame(windows, padx=10, pady=10)
frame.grid(row=3, column=0)

# Create the Listbox inside the Frame
list_box = tk.Listbox(
    frame,
    height=13,
    width=55,
    font=("Arial", 14),
    bd=5,
    relief="sunken",
    highlightthickness=0,
    bg="lightblue"
)
list_box.grid(row=0, column=0, padx=5, pady=(10, 15))  # Adjust grid parameters as needed

# Add some test items to the Listbox with padding
for i in range(20):
    list_box.insert(tk.END, f"  Item {i + 1}  ")  # Add spaces to create padding around the text

# Start the main loop
windows.mainloop()
