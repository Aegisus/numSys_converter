import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        value = int(input_value.get(), base=0)
        if input_var.get() == "Binary":
            value = int(input_value.get(), 2)
        elif input_var.get() == "Hexadecimal":
            value = int(input_value.get(), 16)
        elif input_var.get() == "Decimal":
            value = int(input_value.get(), 10)

        if output_var.get() == "Binary":
            result = bin(value)[2:]
        elif output_var.get() == "Hexadecimal":
            result = hex(value)[2:]
        elif output_var.get() == "Decimal":
            result = str(value)

        output_value.delete(1.0, tk.END)
        output_value.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Number Converter")

input_frame = tk.Frame(root)
output_frame = tk.Frame(root)

input_var = tk.StringVar(value="Binary")
output_var = tk.StringVar(value="Binary")

input_label = tk.Label(input_frame, text="Input:")
input_value = tk.Entry(input_frame)
input_buttons = [tk.Radiobutton(input_frame, text=t, variable=input_var, value=t) for t in ["Binary", "Hexadecimal", "Decimal"]]

output_label = tk.Label(output_frame, text="Output:")
output_value = tk.Text(output_frame, height=4)
output_buttons = [tk.Radiobutton(output_frame, text=t, variable=output_var, value=t) for t in ["Binary", "Hexadecimal", "Decimal"]]

convert_button = tk.Button(root, text="Convert", command=convert)

input_label.pack(side=tk.LEFT)
input_value.pack(side=tk.LEFT)
for button in input_buttons:
    button.pack(side=tk.LEFT)

output_label.pack(side=tk.LEFT)
output_value.pack(side=tk.LEFT)
for button in output_buttons:
    button.pack(side=tk.LEFT)

input_frame.pack(pady=10)
output_frame.pack(pady=10)
convert_button.pack(pady=10)

# Center the window
root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"+{position_right}+{position_top}")

root.mainloop()