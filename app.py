import src
import tkinter as tk
from tkinter import messagebox

def submit():
    # Fetch data from entries
    vars = {
        'model': entry_model.get(),
        'year': entry_year.get(),
        'transmission': entry_transmission.get(),
        'mileage': entry_mileage.get(),
        'fuelType': entry_fuelType.get()
    }

    root.destroy()

    src.main(vars)

# Set up main window
root = tk.Tk()
root.title("Car Data Entry")

# Labels and Entry fields
labels = ['model', 'year', 'transmission', 'mileage', 'fuelType']
def_values = ['0', '2017', '0', '27000', '3']
entries = []

for idx, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky='e')
    entry = tk.Entry(root)
    entry.insert(0, def_values[idx])
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries.append(entry)

entry_model, entry_year, entry_transmission, entry_mileage, entry_fuelType = entries

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=len(labels), column=0, columnspan=2, pady=10)

root.mainloop()