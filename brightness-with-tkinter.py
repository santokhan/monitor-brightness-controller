import screen_brightness_control as sbc
import tkinter as tk
from tkinter import ttk

monitors = sbc.list_monitors()


def change_brightness(value):
    monitor = monitor_combo.get()
    sbc.set_brightness(int(value), display=monitor)
    status_label.config(text=f"{monitor}: {value}%")


root = tk.Tk()
root.title("Brightness Controller")
root.geometry("300x200")

tk.Label(root, text="Select Monitor").pack()

monitor_combo = ttk.Combobox(root, values=monitors)
monitor_combo.pack()
monitor_combo.current(0)

tk.Label(root, text="Brightness").pack()

brightness_slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    command=change_brightness,  # runs when slider changes
)
brightness_slider.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
