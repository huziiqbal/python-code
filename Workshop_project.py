import tkinter as tk
from tkinter import ttk, messagebox


class Crop:
    def __init__(self, crop_id, name, area, cost):
        self.crop_id = crop_id
        self.name = name
        self.area = area
        self.cost = cost


class FarmManager:
    def __init__(self):
        self.crops = []

    def add_crop(self, crop):
        self.crops.append(crop)

    def delete_crop(self, crop_id):
        for crop in self.crops:
            if crop.crop_id == crop_id:
                self.crops.remove(crop)
                return True
        return False

    def get_crops(self):
        return self.crops


manager = FarmManager()


def add_crop():
    crop_id = entry_id.get()
    name = entry_name.get()

    try:
        area = float(entry_area.get())
        cost = float(entry_cost.get())
    except ValueError:
        messagebox.showerror("Error", "Area and Cost must be numbers")
        return

    crop = Crop(crop_id, name, area, cost)
    manager.add_crop(crop)

    refresh_table()

    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_area.delete(0, tk.END)
    entry_cost.delete(0, tk.END)

    messagebox.showinfo("Success", "Crop Added")


def delete_crop():
    crop_id = entry_id.get()

    if manager.delete_crop(crop_id):
        refresh_table()
        messagebox.showinfo("Success", "Crop Deleted")
    else:
        messagebox.showerror("Error", "Crop ID not found")


def update_summary():
    total_area = 0
    total_cost = 0

    for crop in manager.get_crops():
        total_area += crop.area
        total_cost += crop.cost

    summary_label.config(
        text=f"Total Area: {total_area} Acres | Total Cost: ₹{total_cost}"
    )


def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    for crop in manager.get_crops():
        tree.insert(
            "",
            tk.END,
            values=(
                crop.crop_id,
                crop.name,
                crop.area,
                crop.cost
            )
        )

    update_summary()


root = tk.Tk()
root.title("Farmer Crop Management System")
root.geometry("700x550")
root.configure(bg="#d9ead3")

title = tk.Label(
    root,
    text="Farmer Crop Management System",
    font=("Arial", 16, "bold"),
    bg="#d9ead3"
)
title.pack(pady=10)

frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.pack(pady=10, padx=20, fill="x")

tk.Label(frame, text="Crop ID", bg="white").grid(
    row=0, column=0, padx=10, pady=10
)
entry_id = tk.Entry(frame)
entry_id.grid(row=0, column=1)

tk.Label(frame, text="Crop Name", bg="white").grid(
    row=0, column=2, padx=10
)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=3)

tk.Label(frame, text="Area", bg="white").grid(
    row=1, column=0, padx=10, pady=10
)
entry_area = tk.Entry(frame)
entry_area.grid(row=1, column=1)

tk.Label(frame, text="Cost", bg="white").grid(
    row=1, column=2, padx=10
)
entry_cost = tk.Entry(frame)
entry_cost.grid(row=1, column=3)

button_frame = tk.Frame(root, bg="#d9ead3")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add Crop",
    command=add_crop,
    width=12
).grid(row=0, column=0, padx=10)

tk.Button(
    button_frame,
    text="Delete Crop",
    command=delete_crop,
    width=12
).grid(row=0, column=1, padx=10)

tk.Button(
    button_frame,
    text="View Crops",
    command=refresh_table,
    width=12
).grid(row=0, column=2, padx=10)

summary_label = tk.Label(
    root,
    text="Total Area: 0 Acres | Total Cost: ₹0",
    font=("Arial", 11, "bold"),
    bg="#d9ead3"
)
summary_label.pack(pady=5)

tree = ttk.Treeview(
    root,
    columns=("ID", "Name", "Area", "Cost"),
    show="headings",
    height=10
)

tree.heading("ID", text="Crop ID")
tree.heading("Name", text="Crop Name")
tree.heading("Area", text="Area")
tree.heading("Cost", text="Cost")

tree.column("ID", width=100)
tree.column("Name", width=200)
tree.column("Area", width=100)
tree.column("Cost", width=100)

tree.pack(pady=20)

update_summary()

root.mainloop()