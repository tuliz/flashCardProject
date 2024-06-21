from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_english = ""
current_french =""


#---Getting the words from CVS file---
words_dataframe = pandas.read_csv('./data/french_words.csv')
words_dic = words_dataframe.to_dict(orient="records")

#----Function for changing the word from french to english
def change_language():
    canvas.itemconfig(language_text, text='English',fill='white')
    canvas.itemconfig(french_text, text=f'{current_english}',fill='white')
    canvas.itemconfig(card_canvas,image=back_card_image)


#---Get a new random word when buttons are pressed---
def random_word_pick():
    global current_french
    global current_english
    current_card = random.choice(words_dic)
    current_english = current_card['English']
    current_french = current_card['French']
    canvas.itemconfig(language_text,text='French',fill='black')
    canvas.itemconfig(french_text,text=f'{current_french}',fill='black')
    canvas.itemconfig(card_canvas, image=front_card_image)
    window.after(3000, change_language)


#----UI----
window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50,pady=50)

#implementing V button with image
right_image = PhotoImage(file='./images/right.png')
right_btn = Button(image=right_image, highlightthickness=0,command=random_word_pick)
right_btn.grid(row=1,column=1)

#implementing X button with image
wrong_image = PhotoImage(file='./images/wrong.png')
wrong_btn = Button(image=wrong_image, highlightthickness=0,command=random_word_pick)
wrong_btn.grid(row=1, column=0)

#creating canvas with card image and texts for words
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card_image = PhotoImage(file='./images/card_front.png')
back_card_image = PhotoImage(file='./images/card_back.png')
card_canvas = canvas.create_image(400,263,image=front_card_image)
language_text = canvas.create_text(400,150,text='', font=('Ariel',40,'italic'))
french_text = canvas.create_text(400,263, text='', font=('Ariel',60,'bold'))
canvas.grid(row=0,column=0,columnspan=2)

random_word_pick()


window.mainloop()
