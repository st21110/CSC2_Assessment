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

def entrybox_text():

    customer_name.insert(0, "Full Name") #text inside entry box
    def temp_text(e): #function to delete text in entry box
        (customer_name).delete(0,END)
    customer_name.bind("<FocusIn>", temp_text) #Deletes the temporory text once clicked on

    quantity_hired.insert(0, "Item No. (1-500)") #text inside entry box
    def temp_text2(e): #function to delete text in entry box
        (quantity_hired).delete(0,END)
    quantity_hired.bind("<FocusIn>", temp_text2) #Deletes the temporory text once clicked on

    receipt_number.insert(0, "Receipt No.") #text inside entry box
    def temp_text3(e): #function to delete text in entry box
        (receipt_number).delete(0,END)
    receipt_number.bind("<FocusIn>", temp_text3) #Deletes the temporory text once clicked on


#Print details function 
def print_details():
    global total_entries, name_count
    name_count = 0
    
    while name_count < total_entries :
        Label(root, text=name_count).grid(column=0,row=name_count+13) 
        Label(root, text=(customer_details[name_count][0])).grid(column=1,row=name_count+13)
        Label(root, text=(customer_details[name_count][1])).grid(column=2,row=name_count+13)
        Label(root, text=(customer_details[name_count][2])).grid(column=3,row=name_count+13)
        Label(root, text=(customer_details[name_count][3])).grid(column=4,row=name_count+13)
        name_count +=  1

def append_details():
    global customer_details,customer_name,item_hired,quantity_hired,receipt_number,total_entries
    if len(customer_name.get()) != 0:
        customer_details.append([customer_name.get(),item_hired.get(),quantity_hired.get(),receipt_number.get()])
        customer_name.delete(0,END)
        item_hired.set("")
        quantity_hired.delete(0,END)
        receipt_number.delete(0,END)
        total_entries += 1
        entrybox_text()

def delete_row ():
    global customer_details, delete_item, total_entries, name_count
    del customer_details[int(delete_item.get())]
    total_entries = total_entries -1
    delete_item.delete(0,END)
    Label(root, text="                   ").grid(column=0,row=name_count+12) 
    Label(root, text="                   ").grid(column=1,row=name_count+12)
    Label(root, text="                   ").grid(column=2,row=name_count+12)
    Label(root, text="                   ").grid(column=3,row=name_count+12)
    Label(root, text="                   ").grid(column=4,row=name_count+12)
    print_details()

#Buttons
Button(root, text="Append",command=append_details,width=17).grid(row=8,column=3)
Button(root, text="Print Details",command=print_details,width=17).grid(row=8,column=4)
Button(root,text="Quit",command=quit).grid(row=13,column=5)
Button(root,text="Delete",command=delete_row).grid(row=11,column=4)

def main():
    global root, customer_details,total_entries
    entrybox_text()
    customer_details = []
    total_entries = 0
    root.mainloop()


main() 