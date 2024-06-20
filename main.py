from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

#---Getting the words from CVS file---
words_dataframe = pandas.read_csv('./data/french_words.csv')
words_dic = [{'English':row.English,'French':row.French} for (index,row) in words_dataframe.iterrows()]
random_word = random.choice(words_dic)
english_word = random_word['English']
french_word = random_word['French']

#---Get a new random word when buttons are pressed---
def random_func():
    random_word = random.choice(words_dic)
    english_word = random_word['English']
    french_word = random_word['French']
    canvas.itemconfig(french_text,text=f'{french_word}')

#----UI----
window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50,pady=50)

#implementing V button with image
right_image = PhotoImage(file='./images/right.png')
right_btn = Button(image=right_image, highlightthickness=0,command=random_func)
right_btn.grid(row=1,column=1)

#implementing X button with image
wrong_image = PhotoImage(file='./images/wrong.png')
wrong_btn = Button(image=wrong_image, highlightthickness=0,command=random_func)
wrong_btn.grid(row=1, column=0)

#creating canvas with card image and texts for words
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card_image = PhotoImage(file='./images/card_front.png')
canvas.create_image(400,263,image=front_card_image)
canvas.create_text(400,150,text=f'French', font=('Ariel',40,'italic'))
french_text = canvas.create_text(400,263, text=f'{french_word}', font=('Ariel',60,'bold'))
canvas.grid(row=0,column=0,columnspan=2)

window.mainloop()
