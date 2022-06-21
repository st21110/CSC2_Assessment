#Date: 3/6/22
#Author: Prisha

"""
Julie's Party Hire. 

This code will use functions along side methods to produce an outcome. 

"""

#Imports for the project
from tkinter import *
from tkinter import ttk #for nicer boxes and buttons
from tkinter import messagebox #for error messages 

#GUI fonts and colours (so that it can be changed easily in the future or if I wanted to try out a new style)
bg_colour = "OldLace" #background colour
heading_font = "Helvetica 10 bold" #font size and type for headings

#Root settings
root = Tk()
root.title("Julie's Party Hires")
root.config(bg=bg_colour)

#Quit Function
'''
Command for quit button that exits the program.
'''
def quit():
    exit()

#Labels for entries
Label(root, font=(heading_font), text="Customer Name:",bg=bg_colour).grid(row=4,column=2)
Label(root, font=(heading_font), text="Item Hired:",bg=bg_colour).grid(row=5,column=2)
Label(root, font=(heading_font), text="Quantity Hired:",bg=bg_colour).grid(row=6,column=2)
Label(root, font=(heading_font), text="Receipt Number:",bg=bg_colour).grid(row=7,column=2)
Label(root, font=(heading_font), text="Row Number:",bg=bg_colour).grid(row=13,column=2)

#Clear labels to fix placements of headings and entries
Label(root, text="").grid(row=1)
Label(root, text="").grid(row=2)
Label(root, text="").grid(row=14)

#Main title heading
Label(root,text="Julie's Party Hire", font='Arial 25 bold', fg='orange',bg=bg_colour).place(x=120,y=0)

#Instruction sub heading
Label(root,text="Enter Details.", font='Arial 10 bold', fg='red',bg=bg_colour).grid(row=3,column=2)
Label(root,text="Delete Row.", font='Arial 10 bold', fg='red',bg=bg_colour).grid(row=12,column=2)

#List values for item hire (updatable list)
item_names = ["Chairs","Tables","Speakers","Coloured Lights",
"Helium Tanks", "Gas Barbeque","Marquees","Inflatable Pool",
"Bubble Machine","Glassware","Microphone","Karaoke Machine",
"Bouncy Castle","Cake Stand" ,"Fog Machine"]

#Entries
#Customer Name
customer_name = ttk.Entry(root)
customer_name.grid(row=4,column=3) #placement

#Item Hired
items=StringVar()
item_hired = ttk.Combobox(root, textvariable = items, values =(item_names), #comobobox that has values with a list
state = "readonly",width=17) #readonly, so that is uneditable
item_hired.grid(row=5, column=3) #placement

#Quantity Hired
quantity_hired = ttk.Entry(root)
quantity_hired.grid(row=6,column=3) #placement

#Receipt Number
receipt_number = ttk.Entry(root)
receipt_number.grid(row=7,column=3) #placement

#Delete Row
delete_item = ttk.Entry(root)
delete_item .grid(row=13,column=3) #placement

#Entrybox text
'''
Function for text that will appear inside entry boxes that tells the user what infomation is being asked for.
The text inside should be removed/cleared once the user clicks inside the box.
This function will be called everytime the details get appended and when the programn starts.
'''
def entrybox_text():

    customer_name.insert(0, "Full Name") #text inside entry box
    def temp_text(e): #function to delete text in entry box
        (customer_name).delete(0,END)
    customer_name.bind("<FocusIn>", temp_text) #deletes the temporary text once clicked on

    quantity_hired.insert(0, "Item No. (1-500)") #text inside entry box
    def temp_text2(e): #function to delete text in entry box
        (quantity_hired).delete(0,END)
    quantity_hired.bind("<FocusIn>", temp_text2) #deletes the temporary text once clicked on

    receipt_number.insert(0, "Receipt No.") #text inside entry box
    def temp_text3(e): #function to delete text in entry box
        (receipt_number).delete(0,END)
    receipt_number.bind("<FocusIn>", temp_text3) #deletes the temporary text once clicked on

#Entry box text for delete row
'''
Function for text that will appear inside delete item entry box which tells user a number should be entered.
The text inside should be removed/cleared once the user clicks inside the box.
This function will be called everytime a row gets deleted and when the programn starts.
'''
def deleterow_text():
    delete_item.insert(0, "Row No.") #text inside entry box
    def temp_text4(e): #function to delete text in entry box
        (delete_item).delete(0,END)
    delete_item.bind("<FocusIn>", temp_text4) #deletes the temporary text once clicked on

#Print details function 
'''
This function will print the details the user has entered inside the entry boxes and
print the headings the details will be printed under.
'''
def print_details():
    global total_entries, name_count #global variables used
    name_count = 0
    
    #Headings for details printed
    Label(root, font=(heading_font), text="Row #",bg=bg_colour).grid(row=15,column=1)
    Label(root, font=(heading_font), text="Customer Name",bg=bg_colour).grid(row=15,column=2)
    Label(root, font=(heading_font), text="Item Hired",bg=bg_colour).grid(row=15,column=3)
    Label(root, font=(heading_font), text="Quantity Hired",bg=bg_colour).grid(row=15,column=4)
    Label(root, font=(heading_font), text="Receipt Number",bg=bg_colour).grid(row=15,column=5)

    while name_count < total_entries :
        #Labels for details printed
        Label(root,bg=bg_colour, text=name_count).grid(column=1,row=name_count+16) 
        Label(root,bg=bg_colour, text=(customer_details[name_count][0])).grid(column=2,row=name_count+16)
        Label(root,bg=bg_colour, text=(customer_details[name_count][1])).grid(column=3,row=name_count+16)
        Label(root,bg=bg_colour, text=(customer_details[name_count][2])).grid(column=4,row=name_count+16)
        Label(root,bg=bg_colour, text=(customer_details[name_count][3])).grid(column=5,row=name_count+16)
        name_count +=  1

#Append details function
'''
Function that clears all details entered and prepares it for printing
'''
def append_details():
    global customer_details,customer_name,item_hired,quantity_hired,receipt_number,total_entries #global variables used
    if len(customer_name.get()) != 0:
        customer_details.append([customer_name.get(),item_hired.get(),quantity_hired.get(),receipt_number.get()])
        customer_name.delete(0,END)
        item_hired.set("")
        quantity_hired.delete(0,END)
        receipt_number.delete(0,END)
        total_entries += 1
        entrybox_text()

#Delete row function
'''
This function will delete a row which is chosen by the user. 
'''
def delete_row ():
    global customer_details, delete_item, total_entries, name_count
    del customer_details[int(delete_item.get())]
    total_entries = total_entries -1
    delete_item.delete(0,END)
    Label(root, text="                          ", bg = bg_colour).grid(column=1,row=name_count+15)
    Label(root, text="                          ", bg = bg_colour).grid(column=2,row=name_count+15)
    Label(root, text="                          ", bg = bg_colour).grid(column=3,row=name_count+15)
    Label(root, text="                          ", bg = bg_colour).grid(column=4,row=name_count+15)
    Label(root, text="                          ", bg = bg_colour).grid(column=5,row=name_count+15)
    print_details()
    deleterow_text()


#Checking for input errors
'''
Function that checks for input validity 
(makes sure entry isnt empty or something that doesn't meet Julie's requirements)
If an error is present a messagebox displaying the error message will popup. 
Details will not append if input check does not equal 0
'''
def entry_check():
    global customer_name, item_hired, quantity_hired, receipt_number, total_entries #global variables used
    input_check = 0 #variable for checking if errors are present

    #if customer name is empty
    if len(customer_name.get()) == 0:
        messagebox.showerror("Customer name", "Customer full name is required.") #message box with error will pop up
        input_check = 1 #input check will equal 1 

    #if customer name is same as entrybox text
    if customer_name.get() == "Full Name":
        messagebox.showerror("Customer name", "Customer full name is required.") #message box with error will pop up
        input_check = 1 #input check will equal 1 
    
    #if item hired is empty
    if len(item_hired.get()) == 0:
        messagebox.showerror("Item Hired", "Item name is required.") #message box with error will pop up
        input_check = 1 #input check will equal 1 

    try: 
        #if receipt number is same as entrybox text
        if receipt_number.get() == "Receipt No.":
            messagebox.showerror("Receipt Number", "Receipt number is required.") #message box with error will pop up
            input_check = 1 #input check will equal 1 
    
        #if receipt number is empty
        if len(receipt_number.get()) == 0:
            messagebox.showerror("Receipt Number", "Receipt number is required.") #message box with error will pop up
            input_check = 1 #input check will equal 1 
    
        #if receipt number doesnt equal to a number 0>
        if (receipt_number.get().isdigit):
            if int(receipt_number.get()) == 0.9:
                messagebox.showerror("Receipt Number", "Receipt number must be a number.") #message box with error will pop up
                input_check = 1 #input check will equal 1    

    except:#in all other cases (strings or invalid characters)
            messagebox.showerror("Receipt Number", "Receipt number must be a number.") #message box with error will pop up
            input_check = 1 #input check will equal 1      
    
    try:
        #if quantity hired is the same as entrybox text
        if quantity_hired.get() == "Item No. (1-500)":
            messagebox.showerror("Quantity Hired", "Item quantity is required.") #message box with error will pop up
            input_check = 1 #input check will equal 1 

        #if quanitiy hired is empty
        if len(quantity_hired.get()) == 0:
            messagebox.showerror("Quantity Hired", "Item quantity is required.") #message box with error will pop up
            input_check = 1 #input check will equal 1 

        #if quantity hired is 0 or more than 500
        if (quantity_hired.get().isdigit):
            if int(quantity_hired.get()) == 0 or int(quantity_hired.get()) > 500:
                messagebox.showerror("Quantity Hired", "Quantity hired must be between 1 and 500.") #message box with error will pop up
                input_check = 1 #input check will equal 1 
    
    except:#in all other cases (strings or invalid characters)
            messagebox.showerror("Quantity Hired", "Please enter a number.") #message box with error will pop up
            input_check = 1 #input check will equal 1 
    
    #if input check equals 0 there is no errors
    if input_check == 0 : 
        append_details() #details will be appended


#Checking for input errors in delete row
'''
Function checks if entry in delete item is a number.
If invalid character is entered a message box displaying an error message
will popup.
'''
def delete_error():
    global delete_item, total_entries #global variables used
    delete_check = 0 #variable for checking if errors are present
    try:
        #if delete item is the same as entrybox text
        if delete_item.get() == "Row No.":
            messagebox.showerror("Delete Row", "Please enter a row number.") #message box with error will pop up
            delete_check = 1 #delete check will equal 1 

        #if delete item is empty
        if len(delete_item.get()) == 0:
            messagebox.showerror("Delete Row", "Please enter a row number.") #message box with error will pop up
            delete_check = 1 #delete check will equal 1 

        #if delete item number entered does not exist
        if int(delete_item.get()) >= total_entries:
            messagebox.showerror("Delete Row", "That row does not exist.") #message box with error will pop up
            delete_check = 1 #delete check will equal 1 

    except: #in all other cases (string or invalid characters)
        messagebox.showerror("Delete Row", "Please enter a number.") #message box with error will pop up
        delete_check = 1 #delete check will equal 1 

    #if delete check equals 0 there is no errors
    if delete_check == 0:
        delete_row() #row will be deleted

#Buttons
ttk.Button(root, text="Append",command=entry_check,width=20).grid(row=8,column=3)
ttk.Button(root, text="Print Details",command=print_details,width=20).grid(row=8,column=4)
ttk.Button(root,text="Delete",command=delete_error).grid(row=13,column=4)
ttk.Button(root,text="Quit",command=quit).grid(row=13,column=5)

def main():
    global root, customer_details,total_entries
    entrybox_text()
    deleterow_text()
    customer_details = []
    total_entries = 0
    root.mainloop()

main() 