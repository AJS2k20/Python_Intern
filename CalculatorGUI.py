import tkinter as tk

def on_button_click(event):
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif button_text == "C":
        display.delete(0, tk.END)
    else:
        current_text = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current_text + button_text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="black")  # Set the background color to black

# Add an empty row for spacing
empty_row = tk.Label(root, text="", bg="black")
empty_row.grid(row=0, columnspan=4)

# Create an entry widget for the display
display = tk.Entry(root, font=("Arial", 20), bg="white", fg="black")  # Set background and text color
display.grid(row=1, column=0, columnspan=4, padx=5, pady=5)  # Adjust padding and add spacing

# Add another empty row for more spacing
empty_row = tk.Label(root, text="", bg="black")
empty_row.grid(row=2, columnspan=4)

# Define the button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and layout the buttons with centered text
row, col = 3, 0
for button_label in button_labels:
    button = tk.Button(root, text=button_label, padx=20, pady=20, font=("Arial", 20), bg="black", fg="white", anchor='center')
    button.grid(row=row, column=col, padx=5, pady=5)  # Adjust padding
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main loop
root.mainloop()
