import tkinter as tk
from tkinter import ttk
from conversion_data import conversion_data  # Ensure conversion_data.py is in the same directory

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")

        self.input_value = tk.StringVar()
        self.result_value = tk.StringVar()
        self.unit_from = tk.StringVar()
        self.unit_to = tk.StringVar()

        # Input field
        self.input_entry = ttk.Entry(root, textvariable=self.input_value)
        self.input_entry.grid(row=0, column=0, padx=10, pady=10)

        # Dropdown for unit_from
        self.unit_from_menu = ttk.Combobox(root, textvariable=self.unit_from, values=list(self.get_units()))
        self.unit_from_menu.grid(row=0, column=1, padx=10, pady=10)
        self.unit_from_menu.bind("<<ComboboxSelected>>", self.convert)

        # Swap button
        self.swap_button = ttk.Button(root, text="⇄", command=self.swap_units)
        self.swap_button.grid(row=0, column=2, padx=10, pady=10)

        # Dropdown for unit_to
        self.unit_to_menu = ttk.Combobox(root, textvariable=self.unit_to, values=list(self.get_units()))
        self.unit_to_menu.grid(row=0, column=3, padx=10, pady=10)
        self.unit_to_menu.bind("<<ComboboxSelected>>", self.convert)

        # Result field
        self.result_label = tk.Entry(root, textvariable=self.result_value, state="readonly")
        self.result_label.grid(row=0, column=4, padx=10, pady=10)
        self.result_label.configure(state="normal")
        self.result_label.bind("<Button-1>", lambda e: self.result_label.select_range(0, 'end'))

    def get_units(self):
        units = set()
        for key in conversion_data.keys():
            units.add(key[0])
            units.add(key[1])
        return units

    def convert(self, event=None):
        try:
            value = float(self.input_value.get())
            unit_from = self.unit_from.get()
            unit_to = self.unit_to.get()
            if unit_from != unit_to:
                conversion_factor = conversion_data.get((unit_from, unit_to)) or (1 / conversion_data.get((unit_to, unit_from)))
                result = value * conversion_factor
            else:
                result = value
            self.result_value.set(f"{result:.2f}")
        except (ValueError, TypeError):
            self.result_value.set("Invalid input")

    def swap_units(self):
        unit_from = self.unit_from.get()
        unit_to = self.unit_to.get()
        self.unit_from.set(unit_to)
        self.unit_to.set(unit_from)
        self.convert()

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
