from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
marks = ''
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global marks
    global rep
    window.after_cancel(timer)
    canvas.itemconfig(count_text, text='00:00')
    timer_label.config(text="Timer", fg=GREEN)
    marks = ''
    rep = 0
    check_label.config(text=marks)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if rep % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    if rep == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    if rep % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    global marks
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(count_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_session = math.floor(rep / 2)
        for _ in range (work_session):
            marks += '✔'
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
count_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.config(padx=10, pady=5)
reset_button.grid(column=2, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.config(padx=10, pady=5)
start_button.grid(column=0, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)
window.mainloop()
