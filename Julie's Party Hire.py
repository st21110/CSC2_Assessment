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

#List values for item hire (updatable list)
item_names = ["Chairs","Tables","Speakers","Coloured Lights",
"Helium Tanks", "Gas Barbeque","Marquees","Inflatable Pool",
"Bubble Machine","Glassware","Microphone","Karaoke Machine",
"Bouncy Castle","Cake Stand" ,"Fog Machine"]

#Entries

#Customer Name
customer_name = Entry(root)
customer_name.grid(row=4,column=3) #Placement

#Item Hired
items=StringVar()
item_hired = ttk.Combobox(root, textvariable = items, values =(item_names),
state = "readonly",width=17)
item_hired.grid(row=5, column=3)

#Quantity Hired
quantity_hired = Entry(root)
quantity_hired.grid(row=6,column=3)

#Receipt Number
receipt_number = Entry(root)
receipt_number.grid(row=7,column=3)

#Delete Row
delete_item = Entry(root)
delete_item .grid(row=11,column=3)

