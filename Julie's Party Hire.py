#Date: 3/6/22
#Author: Prisha

"""
Julie's Party Hire. 

This code will use functions along side methods to produce an outcome. 

"""

#imports for the project
from tkinter import *
from tkinter import ttk

#Defining and Naming the root
root = Tk()
root.title("Julie's Party Hires")

def quit():
    exit()

#Labels for entries
Label(root, text="Customer Name:").grid(row=4,column=2)
Label(root, text="Item Hired:").grid(row=5,column=2)
Label(root, text="Quantity Hired:").grid(row=6,column=2)
Label(root, text="Receipt Number:").grid(row=7,column=2)
Label(root, text="Row Number:").grid(row=11,column=2)