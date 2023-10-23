from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

#-----------------------------------------------PANDAS----------------------------------------------#
try:
    data = pandas.read_csv("./data/words_left.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
final_list = data.to_dict(orient="records")
print(final_list)
random_word = {}
#--------------------------------------Generating Random Word---------------------------------------#


def change_card():
    global random_word, flip_timmer
    window.after_cancel(flip_timmer)
    canvas.itemconfig(img, image=bg_img)
    random_word = random.choice(final_list)
    french_word = random_word["French"]
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    flip_timmer = window.after(3000, flip_card)


def remove_card():
    global final_list
    final_list.remove(random_word)
    data = pandas.DataFrame(final_list)
    data.to_csv("data/words_left.csv", index=False)
    change_card()


def flip_card():
    new_img = PhotoImage(file="./images/card_back.png")
    canvas.itemconfig(img, image=new_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    eng_word = random_word["English"]
    canvas.itemconfig(word_text, text=eng_word, fill="white")

#-----------------------------------------------UI Setup----------------------------------------------#

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
#window.minsize(height=700, width=800)
window.title("Flashy")
flip_timmer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0)
bg_img = PhotoImage(file="./images/card_front.png")
img = canvas.create_image(370, 263, image=bg_img)
canvas.config(bg=BACKGROUND_COLOR)
title_text = canvas.create_text(400, 150, text="", font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text="", font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=change_card)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=remove_card)
tick_button.grid(row=1, column=1)


change_card()


window.mainloop()

