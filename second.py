import tkinter as tk

# Functions
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Main window
root = tk.Tk()
root.title("Calculator with Buttons")
root.geometry("400x550")
root.configure(bg="#1e1e2f")

expression = ""
equation = tk.StringVar()

# Title Label
title = tk.Label(root, text="Calculator with Buttons",
                 font=("Arial", 18, "bold"),
                 bg="#1e1e2f", fg="cyan")
title.pack(pady=10)

# Frame for center alignment
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(expand=True)

# Display
entry = tk.Entry(frame, textvariable=equation,
                 font=("Arial", 24),
                 bd=10, insertwidth=2,
                 width=15, borderwidth=4,
                 justify="right",
                 bg="black", fg="white")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button style
btn_color = "#2d2d44"
txt_color = "white"

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(frame, text=text, width=5, height=2,
                  font=("Arial", 16),
                  bg="green", fg="white",
                  command=equalpress).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(frame, text=text, width=5, height=2,
                  font=("Arial", 16),
                  bg=btn_color, fg=txt_color,
                  command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(frame, text="C", width=22, height=2,
          font=("Arial", 16),
          bg="red", fg="white",
          command=clear).grid(row=5, column=0, columnspan=4, pady=10)

# Run
root.mainloop()