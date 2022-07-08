BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
from matplotlib import image
from matplotlib.pyplot import text, title
from numpy import record
import pandas as pd
import random

window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def flip_card():
    canvas.itemconfig(card_title, text ="English")
    canvas.itemconfig(card_word, text= random_dict["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)



#calling the window.after method 
flip_timer = window.after(3000, func= flip_card)

try:
#Calling the data file
    data = pd.read_csv("/Users/aryansaini/Documents/Visual Studio Code/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 31/flash-card-project-start/data/french_words.csv")
    data = original_data.to_dict(orient='records')
else:
    data = data.to_dict(orient='records')

#creating a global dict 
random_dict={}

def random_word():
    global random_dict, flip_timer
    window.after_cancel(flip_timer)
    #getting random key value pair
    random_dict = random.choice(data)
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text =random_dict['French'], fill="black")
    canvas.itemconfig(card_background, image = card_front_image)
    flip_timer =  window.after(3000, func= flip_card)
   

def is_known():
    """when the user chicks on check box, is_known
    the function will remove the word from the data
    , create a csv file with the words to learn!"""
    data.remove(random_dict)
    data_ = pd.DataFrame(data)

    data_.to_csv("words_to_learn.csv", index=False)
    random_word()


canvas = Canvas(width =800, height=526)
card_front_image = PhotoImage(file="/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 31/flash-card-project-start/images/card_front.png")
card_back_image = PhotoImage(file="/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 31/flash-card-project-start/images/card_back.png")
card_background =  canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
card_title= canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text= "", font=("Ariel", 40, "bold"))
canvas.grid(column=0,row=0, columnspan=2)

#Creating buttons
cross_image = PhotoImage(file="/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 31/flash-card-project-start/images/wrong.png")
unknown_button = Button(image = cross_image , highlightthickness=0, command=random_word)
unknown_button.grid(column=0, row=1)


check_image = PhotoImage(file="/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 31/flash-card-project-start/images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(column=1, row=1)

random_word()







window.mainloop()
