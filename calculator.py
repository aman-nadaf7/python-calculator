print("Calculator started!")

import tkinter as tk

# Initialize main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")
root.config(bg="#1e1e1e")

expression = ""

def update_display(symbol):
    global expression
    expression += str(symbol)
    display_var.set(expression)

def clear_display():
    global expression
    expression = ""
    display_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate_result():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""

def animate_button(char):
    btn = button_refs.get(char)
    if not btn:
        return
    original_bg = btn['bg']
    btn.config(bg="#777777")
    btn.after(100, lambda: btn.config(bg=original_bg))

def key_handler(event):
    key = event.keysym

    if key in '0123456789':
        update_display(key)
    elif key in ['plus', 'KP_Add']:
        update_display('+')
    elif key in ['minus', 'KP_Subtract']:
        update_display('-')
    elif key in ['asterisk', 'KP_Multiply']:
        update_display('*')
    elif key in ['slash', 'KP_Divide']:
        update_display('/')
    elif key == 'period':
        update_display('.')
    elif key == 'Return':
        calculate_result()
    elif key == 'BackSpace':
        backspace()
    elif key in ['Escape', 'c']:
        clear_display()

    key_map = {
        'Return': '=',
        'BackSpace': '⌫',
        'Escape': 'Clear',
        'c': 'Clear',
        'plus': '+', 'KP_Add': '+',
        'minus': '-', 'KP_Subtract': '-',
        'asterisk': '*', 'KP_Multiply': '*',
        'slash': '/', 'KP_Divide': '/',
        'period': '.'
    }

    char = key if key in '0123456789' else key_map.get(key)
    if char:
        animate_button(char)

# Display This creates a big white box at the top to show what you're typing and the result.
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 24), justify='right', bd=10, relief='flat')
display.pack(fill='both', ipadx=8, ipady=15, padx=10, pady=10)

# Buttons Frame using grid layout
buttons_frame = tk.Frame(root, bg="#1e1e1e")
buttons_frame.pack(expand=True, fill='both')

buttons = [
    ['7', '8', '9', '⌫'],
    ['4', '5', '6', '/'],
    ['1', '2', '3', '*'],
    ['0', '.', '+', '-'],
    ['=', 'Clear']
]

button_refs = {}

# Grid layout
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if char == '=':
            command = calculate_result
        elif char == 'Clear':
            command = clear_display
        elif char == '⌫':
            command = backspace
        else:
            command = lambda x=char: update_display(x)

        b = tk.Button(buttons_frame, text=char, command=command,
                      font=("Helvetica", 16),
                      bg="#3c3f41", fg="white",
                      activebackground="#5a5d5f",
                      activeforeground="white",
                      bd=0, relief='flat')

        button_refs[char] = b

        b.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

# Make all rows and columns expand evenly
for i in range(5):  # 5 rows
    buttons_frame.rowconfigure(i, weight=1)
for i in range(4):  # 4 columns max
    buttons_frame.columnconfigure(i, weight=1)

# Bind keyboard keys
root.bind("<Key>", key_handler)

# Run the app
root.mainloop()
