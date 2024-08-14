#Date 9/8/24
# 4th ver of julie's party hire

#imports tkinter to create GUI

from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
import os

#Quit function
def quit():
    main_window.destroy()

def info():
    name_details= full_name.get()
    party_items= party_items.get()
    items_hired= items_hired.get()
    receipet_number= receipet_number.get()

    print(name_details, party_items,receipet_number)

    with open("reciepts.txt", "w") as file:

        file.write(f"{full_name},  {party_items}, {items_hired}\n")



def enteries():

    name_count = 0

    Label(main_window, font=("Helvetica 10 bold"), text="Row").grid(column=0,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Full Name").grid(column=1,row=7)   
    Label(main_window, font=("Helvetica 10 bold"),text="Party Items").grid(column=2,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Items Hired").grid(column=3,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Reciept No").grid(column=4,row=7)

    while name_count < counters['total_entries'] :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8) 
        
        Label(main_window, text=(enteries[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(enteries[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=(enteries[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1
        counters['name_count'] = name_count

def check_inputs ():
    input_check = 0
    Label(main_window, text="               ") .grid(column=2,row=0)
    Label(main_window, text="               ") .grid(column=2,row=1)
    Label(main_window, text="               ") .grid(column=2,row=2)
    Label(main_window, text="               ") .grid(column=2,row=3)

    if (full_name.get())== "":
        Label(main_window, fg="#7b5bc6", text= "REQUIRED").grid(column=2,row=0)
        input_check = 1

    if len(combo_party_items.get())== 0:
        Label(main_window, fg="#7b5bc6", text= "REQUIRED").grid(column=2,row=1)
        input_check = 1

    if len(items_hired.get())== 0:
        Label(main_window, fg="#7b5bc6", text= "REQUIRED").grid(column=2,row=2)
        input_check = 1



    if input_check == 0 : append_name()



    

def append_name():

    enteries.append([full_name.get(), combo_party_items.get(), items_hired.get()])


    full_name.delete(0, 'end')

    combo_party_items.set('')  # Clears combo box

    items_hired.delete(0, 'end')

    counters['total_entries'] += 1


def delete_row():
    del enteries[int(delete_item.get())]
    counters['total_entries'] -= 1
    name_count = counters['name_count']
    delete_item.delete(0,'end')
    
    Label(main_window, text="       ").grid(column=0,row=name_count+7) 
    Label(main_window, text="       ").grid(column=1,row=name_count+7)
    Label(main_window, text="       ").grid(column=2,row=name_count+7)
    Label(main_window, text="       ").grid(column=3,row=name_count+7)
    Label(main_window, text="       ").grid(column=4,row=name_count+7)

    print_enteries()

   
def setup_buttons():   
    Button(main_window, text="Quit",command=quit,width = 10) .grid(column=4, row=0,sticky=E)
    Button(main_window, text="Submit", bg="#b3a2d8",command=check_inputs) .grid(column=3,row=1)
    Button(main_window, text="Print Details",command= enteries,width = 10) .grid(column=4,row=1,sticky=E)
    Label(main_window, bg ='#d3c5f3',font=("Helvetica 10 bold"), text= "Full Name"). grid (column= 0, row=0, sticky=E)
    Label(main_window, bg ='#d3c5f3', font=("Helvetica 10 bold"), text="Party Items") .grid(column=0,row=1,sticky=E)
    Label(main_window, bg ='#d3c5f3', font=("Helvetica 10 bold"), text="Items Hired") .grid(column=0,row=2,sticky=E)
    Label(main_window, bg ='#d3c5f3', font=("Helvetica 10 bold"),text="Reciept No").grid(column=0, row=3, sticky=E)


    
    Label(main_window, text="Row #") .grid(column=3,row=2,sticky=E)
    Button(main_window, text="Delete Row",command=delete_row,width = 10) .grid(column=4,row=3,sticky=E)
    




def main():
    setup_buttons()
    main_window.mainloop()


counters = {'total_entries':0,'name_count':0}
enteries=[]

main_window =Tk()
main_window.geometry("490x200")
main_window.title("Julie's Party Store")

main_window.configure(background="#d3c5f3")

full_name = Entry(main_window)

full_name.grid(column=1, row=0)




combo_party_items = ttk.Combobox(main_window, values=["Balloons", "Confetti", "Clowns", "Cups", "Cutlery", "Party Hats"])
combo_party_items.grid(column=1, row=1)


items_hired = Entry(main_window)

items_hired.grid(column=1, row=2)


delete_item = Entry(main_window)

delete_item.grid(column=3, row=3)

 



main()
