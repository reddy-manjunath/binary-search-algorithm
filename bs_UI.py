import tkinter as tk
from tkinter import messagebox

# Binary Search Algorithm
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Function to perform search when button is clicked
def perform_search():
    try:
        target = int(entry_target.get())
        arr = sorted([int(i) for i in entry_list.get().split(',')])
        result = binary_search(arr, target)
        if result != -1:
            messagebox.showinfo("Success", f"Element {target} found at position {result+1}")
        else:
            messagebox.showwarning("Not Found", f"Element {target} not found in the list")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Main Tkinter window
root = tk.Tk()
root.title("Binary Search Visualizer")
root.geometry("400x400")
root.configure(bg='#282828')

# Title label
title_label = tk.Label(root, text="Binary Search Visualizer", font=("Helvetica", 20, 'bold'), fg='white', bg='#282828')
title_label.pack(pady=20)

# Input list section
frame_list = tk.Frame(root, bg='#282828')
frame_list.pack(pady=10)

label_list = tk.Label(frame_list, text="Enter a sorted list (comma-separated):", font=("Helvetica", 12), fg='white', bg='#282828')
label_list.pack(side=tk.LEFT, padx=10)

entry_list = tk.Entry(frame_list, width=20, font=("Helvetica", 12), bd=2)
entry_list.pack(side=tk.LEFT)

# Target number section
frame_target = tk.Frame(root, bg='#282828')
frame_target.pack(pady=10)

label_target = tk.Label(frame_target, text="Enter number to search:", font=("Helvetica", 12), fg='white', bg='#282828')
label_target.pack(side=tk.LEFT, padx=10)

entry_target = tk.Entry(frame_target, width=10, font=("Helvetica", 12), bd=2)
entry_target.pack(side=tk.LEFT)

# Search button
search_button = tk.Button(root, text="Search", command=perform_search, font=("Helvetica", 14), bg='#4CAF50', fg='white', bd=0)
search_button.pack(pady=20)

# Footer
footer_label = tk.Label(root, text="Developed by R.Manjunath ", font=("Helvetica", 10), fg='white', bg='#282828')
footer_label.pack(side=tk.BOTTOM, pady=10)

# Run the application
root.mainloop()
