from tkinter import Tk, Button, Label, DoubleVar, Entry

# Create the main window
window = Tk()
window.title("Feet to Meter Conversion App")
window.configure(background="light green")
window.geometry("320x220")
window.resizable(width=False, height=False)

# Function to perform the conversion
def convert():
    try:
        value = float(ft_entry.get())
        meter = value * 0.3048
        mt_value.set(f"{meter:.4f}")
    except ValueError:
        mt_value.set("Invalid input")

# Function to clear the input and output fields
def clear():
    ft_value.set("")
    mt_value.set("")

# Variables for storing user input and result
ft_value = DoubleVar()
mt_value = DoubleVar()

# Labels and Entries for user input and displaying the result
ft_lb = Label(window, text="Feet", bg="purple", fg="white", width=14)
ft_lb.grid(row=0, column=0, padx=15, pady=15)

ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, 'end')

mt_lbl = Label(window, text="Meter", bg="brown", fg="white", width=14)
mt_lbl.grid(column=0, row=1)

mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(column=1, row=1, pady=30)
mt_entry.delete(0, 'end')

# Button to trigger the conversion
convert_btn = Button(window, text="Convert", bg="blue", fg="white", width=14, command=convert)
convert_btn.grid(column=0, row=3, padx=25)

# Button to clear the input and output fields
clear_btn = Button(window, text="Clear", bg="black", fg="white", width=14, command=clear)
clear_btn.grid(column=1, row=3, padx=25)

# Start the Tkinter event loop
window.mainloop()