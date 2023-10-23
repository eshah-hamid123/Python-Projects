from tkinter import *
#window
window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#label

my_label = Label(text="First Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.config(padx=20, pady=0)
my_label.grid(column=0, row=0)
#my_label.place(x=100, y=-100)

#button

def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input )


button = Button(text="Click me", command=button_clicked)
button.grid(column=0, row=1)

#Entry

input = Entry(width=30)
input.insert(END, string="Some text to begin with")
input.grid(column=2, row=0)

#Text
text = Text(height=3, width=20)
text.focus()
text.insert(END, "This is a textbox")
print(text.get('1.0', END))
text.grid(column=2, row=3)

#spinbox


def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used )
spinbox.grid(column=0, row=3)

#scale


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=3, row=1)

#checkbutton


def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state,command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=0, row=5)

#radiobutton


def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton.grid(column=0, row=5)
radiobutton2.grid(column=0, row=6)


#listbox


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=3, row=7)
window.mainloop()

