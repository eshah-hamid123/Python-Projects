from tkinter import *

window = Tk()

window.title("Mile-Kilometer Converter")
window.minsize(width=500, height=200)
window.config(padx=50, pady=50)

input = Entry(width = 20)
input.grid(column=1, row=0)


mile_label = Label(text="Miles", font=("Arial", 18, "normal"))
mile_label.config(padx=10, pady=10)
mile_label.grid(column=3, row=0)


equal_label = Label(text="Is equal to", font=("Arial", 18, "normal"))
#equal_label.config(padx=10, pady=10)
equal_label.grid(column=0, row=1)


converted_label = Label(text="0", font=("Arial", 18, "normal"))
converted_label.grid(column=1, row=1)

km_label = Label(text="km", font=("Arial", 18, "normal"))
km_label.grid(column=2, row=1)

def button_clicked():
    user_input = input.get()
    ans = int(user_input) / 0.621371
    ans = int(ans)
    converted_label.config(text=ans)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()