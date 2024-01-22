from tkinter import *
import random
import pandas

BACKGROUND = "#B1DDC6"
card = {}
words = {}

try:
    toLearn_csv = pandas.read_csv("words_tolearn.csv")
except FileNotFoundError:
    original_csv = pandas.read_csv("german_words.csv")
    words = original_csv.to_dict(orient="records")
else:
    words = toLearn_csv.to_dict(orient="records")
# we create a list of dictionaries using orient= records

def next_word():
    global card,flip_time
    window.after_cancel(flip_time)
    card = random.choice(words)
    canvas.itemconfig(card_title,text="German",fill="black")
    canvas.itemconfig(card_word,text=card["German"],fill="black")
    canvas.itemconfig(card_img,image=front_img)
    flip_time =window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_img, image= back_img)
    canvas.itemconfig(card_title,text="English",fill= "white")
    canvas.itemconfig(card_word, text=card["English"],fill="white")

def remove_known():
    words.remove(card)
    next_word()
    data = pandas.DataFrame(words)
    data.to_csv("words_tolearn.csv",index=False)
    next_word()

window = Tk()
window.title("German flashcards")
window.minsize(600,600)
window.config(padx=20,pady=20,bg=BACKGROUND)
flip_time = window.after(3000,func= flip_card)

canvas = Canvas(height=526,width=800,bg=BACKGROUND,highlightthickness=0)
front_img = PhotoImage(file="card_front.png")
back_img =PhotoImage(file="card_back.png")
card_img = canvas.create_image(400,263,image= front_img)
card_title = canvas.create_text(400,150,text="title",font=("Times New Roman",35))
card_word = canvas.create_text(400,260, text="word",font=("Times New Roman",70,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img,highlightthickness=0,command=next_word)
wrong_button.grid(row=1,column=0)

right_img = PhotoImage(file="right.png")
right_button =Button(image=right_img,highlightthickness=0,command=remove_known)
right_button.grid(row=1,column=1)

next_word()

window.mainloop()