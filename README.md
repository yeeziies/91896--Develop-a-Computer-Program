# complete version  
#imports tkinter to create GUI

from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import random
import os

#Quit function
def quit():
    main_window.destroy()

def photo():
    

    gif= PhotoImage(file="C:/Users/21300/OneDrive - Lynfield College/Documents/2PAD 2024/fdshfbhjdsvfdsjf.png")

    gif_label= Tk.Label(main_window,image=gif)
    gif_label.grid(column=0, row=5)

    gif_label.image= gif


def info_entries():

    name_count = 0

    Label(main_window, font=("Helvetica 10 bold"), text="Row").grid(column=0,row=7)
    Label(main_window, font=("Helvetica 10 bold"),fg ="#ffe2ef", text="Full Name").grid(column=1,row=7)  
    Label(main_window, font=("Helvetica 10 bold"),text="Party Items").grid(column=2,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Items Hired").grid(column=3,row=7)
    Label(main_window, font=("Helvetica 10 bold"),text="Reciept No").grid(column=4,row=7)

    while name_count < counters['total_entries'] :
        Label(main_window, text=name_count).grid(column=0,row=name_count+8)
        Label(main_window, text=(entries[name_count][0])).grid(column=1,row=name_count+8)
        Label(main_window, text=(entries[name_count][1])).grid(column=2,row=name_count+8)
        Label(main_window, text=(entries[name_count][2])).grid(column=3,row=name_count+8)
        Label(main_window, text=(entries[name_count][3])).grid(column=4,row=name_count+8)
        name_count +=  1
        counters['name_count'] = name_count

def check_inputs ():
    input_check = 0
    Label(main_window, text="               ") .grid(column=2,row=0)
    Label(main_window, text="               ") .grid(column=2,row=1)
    Label(main_window, text="               ") .grid(column=2,row=2)
    Label(main_window, text="               ") .grid(column=2,row=3)

    if (full_name.get())== "":
        Label(main_window, fg="#eb1979", text= "REQUIRED").grid(column=2,row=0)
        input_check = 1

    if len(combo_party_items.get())== 0:
        Label(main_window, fg="#eb1979", text= "REQUIRED").grid(column=2,row=1)
        input_check = 1

    if len(items_hired.get())== 0:
        Label(main_window, fg="#eb1979", text= "REQUIRED").grid(column=2,row=2)
        input_check = 1

    if input_check == 0 :
        append_name()


def append_name():

    receipt_number= random.randint(1,10000) #creates random number gen with the limit of 1-10000
   
    entries.append([full_name.get(), combo_party_items.get(), items_hired.get(), receipt_number])

   
    full_name.delete(0, 'end')

    combo_party_items.set('')  # Clears combo box

    items_hired.delete(0, 'end')

    counters['total_entries'] += 1
   

def delete_row():
    # find which row is to be deleted and delete it

    del entries[int(delete_item.get())]

    counters['total_entries'] -= 1

    name_count = counters['name_count']

    delete_item.delete(0, 'end')

    # clear the last item displayed on the GUI

    Label(main_window, text="       ").grid(column=0, row=name_count + 7)

    Label(main_window, text="       ").grid(column=1, row=name_count + 7)

    Label(main_window, text="       ").grid(column=2, row=name_count + 7)

    Label(main_window, text="       ").grid(column=3, row=name_count + 7)

    Label(main_window, text="       ").grid(column=4, row=name_count + 7)

    Label(main_window, text="       ").grid(column=5, row=name_count + 7)

    info_entries()




   
def setup_buttons():
    Label(main_window, bg ='#ffebf9',font=("Helvetica 10 bold"), text= "Full Name"). grid (column= 0, row=0, sticky=E)
    Label(main_window, bg ='#ffebf9', font=("Helvetica 10 bold"), text="Party Items") .grid(column=0,row=1,sticky=E)
    Label(main_window, bg ='#ffebf9', font=("Helvetica 10 bold"), text="Items Hired") .grid(column=0,row=2,sticky=E)
    Label(main_window, bg ='#ffebf9', font=("Helvetica 10 bold"),text="Reciept No").grid(column=0, row=3, sticky=E)

    Button(main_window, text="Quit",command=quit,width = 10) .grid(column=4, row=0,sticky=E)
    Button(main_window, text="Submit", bg="#f1cde7",command=check_inputs) .grid(column=3,row=1)
    Button(main_window, text="Print Details",command= info_entries,width = 10) .grid(column=4,row=1,sticky=E)
   
    Label(main_window, text="Row #") .grid(column=3,row=2,sticky=E)
    Button(main_window, text="Delete Row",command=delete_row,width = 10) .grid(column=4,row=3,sticky=E)
   


def main():


    setup_buttons()
    photo()
    main_window.mainloop()

counters = {'total_entries':0,'name_count':0}
entries=[]
photo()
main_window =Tk()
main_window.geometry("550x500")
main_window.title("Julie's Party Store")




main_window.configure(background="#ffebf9")

full_name = Entry(main_window)

full_name.grid(column=1, row=0)


combo_party_items = ttk.Combobox(main_window, values=["Balloons","Candy", "Confetti", "Clowns", "Cups", "Cutlery","Fairy Lights","Glassware", "Party Hats","Table Decorations",])
combo_party_items.grid(column=1, row=1)


items_hired = Entry(main_window)

items_hired.grid(column=1, row=2)


delete_item = Entry(main_window)

delete_item.grid(column=3, row=3)



 


main()
