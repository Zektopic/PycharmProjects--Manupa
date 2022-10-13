#!/usr/bin/python

import tkinter
top = tkinter.Tk()
top.title("Manupa's 1st GUI")
# Code to add widgets will go here...
label = tkinter.Label(top, text = "Hello World" ,font =("Arial Bold",50)).pack()
top.geometry('1920x1080')
#Here we define a variable to act as the label displayed on the window as "Hello World
bt = tkinter.Button (top,text="Hack!")
bt.grid(column = 1 ,row = 0)
#This represents the the button as "Hack"
top.mainloop()
#This ends the program drawning code from the library