import tkinter 
import cv2
import PIL.Image, PIL.ImageTk 
import threading
import time
import imutils
import random

def play():
    frame = cv2.cvtColor(cv2.imread("spinning.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

    lst= "Dice1.png","Dice2.png","Dice3.png","Dice4.png","Dice5.png","Dice6.png"
    img = random.choice(lst)
    
    frame = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    

SET_WIDTH = 526
SET_HEIGHT = 530


window = tkinter.Tk()
window.title("Dice Simulator")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()

btn = tkinter.Button(window, text="Roll The Dice", width=50, command=play)
btn.pack()

window.mainloop()