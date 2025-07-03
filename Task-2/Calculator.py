import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation_var.get()
        
        if op == '+': result = num1 + num2
        elif op == '-': result = num1 - num2
        elif op == '*': result = num1 * num2
        elif op == '/': 
            if num2 == 0:
                messagebox.showerror("Error", "Can't divide by zero!")
                return
            result = num1 / num2
            
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("280x300")

tk.Label(root, text="First Number:").pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

tk.Label(root, text="Second Number:").pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

tk.Label(root, text="Operation:").pack()
operation_var = tk.StringVar(value='+')

for text, op in [('+ Addition', '+'), ('- Subtraction', '-'), 
                 ('* Multiplication', '*'), ('/ Division', '/')]:
    tk.Radiobutton(root, text=text, variable=operation_var, value=op).pack(anchor='w')

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
result_label = tk.Label(root, text="Result: ", font=('Arial', 12))
result_label.pack()

root.mainloop()
