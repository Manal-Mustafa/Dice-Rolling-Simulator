from tkinter import *
from PIL import Image
from PIL import ImageTk
import random

# toplevel widget which represents the main window of an application
window = Tk()
window.geometry('400x400')
window.resizable(0,0)
window.title('Manal - Roll the Dice')
window.configure(background='white')

# Adding label into the frame
l0 = Label(window, text="",bg='white')
l0.pack()

# adding label with different font and formatting
l1 = Label(window, text="Hello from MM!", fg = "red",
        bg = "black",
        font = "Helvetica 16 bold italic")
l1.pack()
l2 = Label(window, text="",bg='white')
l2.pack()
# images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# simulating the image1 with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = Label(window, image=image1)
label1.image = image1

# packing a widget in the parent widget
label1.pack( )

# function activated by button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1


# adding button, and command will use rolling_dice function
button = Button(window, text='Roll the Dice', font='Helvetica 10 bold italic',fg='red', bg='black',command=rolling_dice)

# pack a widget in the parent widget
button.pack( )

# call the mainloop of Tk
# keeps window open
window.mainloop()