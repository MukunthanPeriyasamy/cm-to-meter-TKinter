from tkinter import *

def cm_to_m():
    convert = float(input.get())
    int_value = convert
    meter = int_value / 100
    output.config(text=f" {convert} cm is equal to {meter} m:")

window = Tk()
window.title("cm to m Converter")
window.minsize(width=300,height=200)

my_tk = Label(text="Enter the Centimeter value")
my_tk.grid(column = 0,row=0)

cm = Label(text="cm :")
cm.grid(column = 0,row=1)
cm.config(pady=10)

input = Entry(width=10)
input.grid(column= 0,row=1)

output = Label(text="is equal to 0 m:")
output.grid(column = 0,row=3)

button = Button(text="convert",command=cm_to_m)
button.grid(column=4,row=1)
button.config(padx=5)

window = mainloop()
