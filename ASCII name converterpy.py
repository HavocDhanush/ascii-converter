# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:04:07 2024

@author: Dhanush N
"""

from tkinter import *

root = Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = "snow")


enter_word = Entry(root)
enter_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label = Label(root, text = "Name in Ascii : ", bg = "light yellow", fg = "black")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        
def clearButton():
    label.config(text="Name in Ascii : ")

btn = Button(root, text = "Show name in Ascii", command = asciiConverter, bg='gold', fg='black')
btn1 = Button(root, text = "Clear", command = clearButton, bg='gold', fg='black')
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
btn1.place(relx = 0.5, rely = 0.8, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)



root.mainloop()

