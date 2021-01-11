# Event Driven GUI Program
import tkinter
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
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_clicked():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    REPS += 1
    print(REPS)
    if REPS % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_clicked()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += " ✔"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title Label
title = tkinter.Label(text="Timer",
                      fg=GREEN,
                      bg=YELLOW,
                      font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

# Image
canvas = tkinter.Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103,
                                130,
                                text="00:00",
                                fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start = tkinter.Button(text="Start",
                       command=start_clicked,
                       highlightthickness=0)
start.grid(column=0, row=2)

# Reset Button
reset = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=2)

# Checkmark
checkmarks = tkinter.Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()
