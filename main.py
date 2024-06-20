from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


#----UI----
window = Tk()
window.title('Flash Cards')
window.config(bg=BACKGROUND_COLOR, padx=50,pady=50)

#implementing V button with image
right_image = PhotoImage(file='./images/right.png')
right_btn = Button(image=right_image, highlightthickness=0)
right_btn.grid(row=1,column=1)

#implementing X button with image
wrong_image = PhotoImage(file='./images/wrong.png')
wrong_btn = Button(image=wrong_image, highlightthickness=0)
wrong_btn.grid(row=1, column=0)

#creating canvas with card image and texts for words
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card_image = PhotoImage(file='./images/card_front.png')
canvas.create_image(400,263,image=front_card_image)
canvas.create_text(400,150,text='English', font=('Ariel',40,'italic'))
canvas.create_text(400,263, text='Word', font=('Ariel',60,'bold'))
canvas.grid(row=0,column=0,columnspan=2)

window.mainloop()
