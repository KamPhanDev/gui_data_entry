import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Create a new tkinter window
window = tk.Tk()
window.title("User Information")

# Create tkinter variables for name and age
name_var = tk.StringVar()
age_var = tk.StringVar()

# Function to save name and age to excel
def save_info():
    name = name_var.get()
    age = age_var.get()

    # Create a DataFrame and write to excel
    df = pd.DataFrame({"Name": [name], "Age": [age]})
    df.to_excel("user_info.xlsx", index=False)

    # Show success message and clear inputs
    messagebox.showinfo("Success", "Information saved successfully!")
    name_var.set("")
    age_var.set("")

# Create name label and entry
name_label = tk.Label(window, text="Name")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window, textvariable=name_var)
name_entry.grid(row=0, column=1)

# Create age label and entry
age_label = tk.Label(window, text="Age")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(window, textvariable=age_var)
age_entry.grid(row=1, column=1)

# Create save button
save_button = tk.Button(window, text="Save", command=save_info)
save_button.grid(row=2, column=1)

# Run the tkinter window loop
window.mainloop()
