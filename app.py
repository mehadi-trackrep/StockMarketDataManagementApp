from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import csv
import os
import json
# from database_utils import *

import mysql.connector

##TODO - Database
mydb = mysql.connector.connect(host="localhost", user="root", passwd=None, port=3306, database="tkinter",
                               auth_plugin="mysql_native_password")
cursor = mydb.cursor()

def add_new():
    pass

##TODO - Applicaiton Starts here
root = Tk()
q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()
t10 = StringVar()
t11 = StringVar()
t12 = StringVar()
t13 = StringVar()
t14 = StringVar()
t15 = StringVar()


wrapper1 = LabelFrame(root, text="Category Section", font=("Arial", 25))
wrapperr3 = LabelFrame(root, text="Customer Data", font=("Arial", 25))
#
# wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
# wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper1.pack(fill="both", expand="yes", padx=20, pady=20)
wrapperr3.pack(fill="both", expand="yes", padx=20, pady=20)

###TODO- combobox
clicked = StringVar()

# Label
ttk.Label(wrapper1, text="Select the Category: ",
          font=("Times New Roman", 15)).grid(column=1,
                                             row=2, padx=10, pady=25)

monthchoosen = ttk.Combobox(wrapper1, state="readonly", width=27,
                            textvariable=clicked)

# Adding combobox drop down list
monthchoosen['values'] = ("Solar System",
                            "Mega Spares",
                            "Inverter",
                            "Motors B3 & V1",
                            "Engine+Generator+Milling Mach",
                            "Allied Pump Motor Set",
                            "Submersible",
                            "KRT+Amarex+Movi",
                            "Centrifugal Pumps & Etabloc",
                            "Booster Pump Set",
                            "Sandpiper",
                            "Chemical",
                            "Gear Viking Pump Motor",
                            "Pulsafedder",
                            "Water Meter",
                            "Valves",
                            "Strainers & Pipes",
                            "Flexible Joint"
                          )
# b1 = tk.Button(wrapper,  text='Show Value', command=lambda: my_show())
# b1.grid(row=2,column=6)
#
# str_out= StringVar()
# str_out.set("Output")
#
# l2 = tk.Label(wrapper,  textvariable=str_out, width=10)
# l2.grid(row=2,column=7)
#
# def my_show():
#     str_out.set(clicked.get())

monthchoosen.grid(column=3, row=2)
monthchoosen.current(2)

var = StringVar()
lbl = Label(wrapper1, text="Create Category", font=("Helvetica", 15))
lbl.grid(row=2, column=4, padx=25, pady=6)
ent = Entry(wrapper1, textvariable=var)
ent.grid(row=2, column=5, padx=5, pady=6)

print("Chosen value: ",clicked.get())


#TODO - User Data Selection
wrapper3 = Frame(wrapperr3, bg="gray")
wrapper3.pack(fill="both", expand="yes", padx=20, pady=20)

lbl1 = Label(wrapper3, text="Model Name *", font=("Helvetica", 15))
lbl1.grid(row=0, column=0, padx=5, pady=10)
ent1 = Entry(wrapper3, textvariable=t1)
ent1.grid(row=0, column=1, padx=5, pady=10)

lbl2 = Label(wrapper3, text="Date", font=("Helvetica", 15))
lbl2.grid(row=1, column=0, padx=5, pady=6)
ent2 = Entry(wrapper3, textvariable=t2)
ent2.grid(row=1, column=1, padx=5, pady=6)

lbl3 = Label(wrapper3, text="Balancing Figure", font=("Helvetica", 15))
lbl3.grid(row=2, column=0, padx=5, pady=6)
ent3 = Entry(wrapper3, textvariable=t3)
ent3.grid(row=2, column=1, padx=5, pady=6)

lbl4 = Label(wrapper3, text="Received Quantity", font=("Helvetica", 15))
lbl4.grid(row=3, column=0, padx=5, pady=6)
ent4 = Entry(wrapper3, textvariable=t4)
ent4.grid(row=3, column=1, padx=5, pady=6)

lbl5 = Label(wrapper3, text="Return Challan", font=("Helvetica", 15))
lbl5.grid(row=4, column=0, padx=5, pady=6)
ent5 = Entry(wrapper3, textvariable=t5)
ent5.grid(row=4, column=1, padx=5, pady=6)

lbl6 = Label(wrapper3, text="Remarks", font=("Helvetica", 15))
lbl6.grid(row=0, column=2, padx=5, pady=10)
ent6 = Entry(wrapper3, textvariable=t6)
ent6.grid(row=0, column=3, padx=5, pady=10)

lbl7 = Label(wrapper3, text="GatePass Serial Number(SN)", font=("Helvetica", 15))
lbl7.grid(row=1, column=2, padx=5, pady=6)
ent7 = Entry(wrapper3, textvariable=t7)
ent7.grid(row=1, column=3, padx=5, pady=6)

lbl8 = Label(wrapper3, text="Acceptance Of Order SN", font=("Helvetica", 15))
lbl8.grid(row=2, column=2, padx=5, pady=6)
ent8 = Entry(wrapper3, textvariable=t8)
ent8.grid(row=2, column=3, padx=5, pady=6)

lbl9 = Label(wrapper3, text="Delivery Challan SN", font=("Helvetica", 15))
lbl9.grid(row=3, column=2, padx=5, pady=6)
ent9 = Entry(wrapper3, textvariable=t9)
ent9.grid(row=3, column=3, padx=5, pady=6)

lbl10 = Label(wrapper3, text="QuantityIssued", font=("Helvetica", 15))
lbl10.grid(row=4, column=2, padx=5, pady=6)
ent10 = Entry(wrapper3, textvariable=t10)
ent10.grid(row=4, column=3, padx=5, pady=6)

lbl11 = Label(wrapper3, text="Balance Quantity", font=("Helvetica", 15))
lbl11.grid(row=0, column=4, padx=5, pady=10)
ent11 = Entry(wrapper3, textvariable=t11)
ent11.grid(row=0, column=5, padx=5, pady=10)

lbl12 = Label(wrapper3, text="Marketing Person", font=("Helvetica", 15))
lbl12.grid(row=1, column=4, padx=5, pady=6)
ent12 = Entry(wrapper3, textvariable=t12)
ent12.grid(row=1, column=5, padx=5, pady=6)

lbl13 = Label(wrapper3, text="Party Name(LetterOfCredit)", font=("Helvetica", 15))
lbl13.grid(row=2, column=4, padx=5, pady=6)
ent13 = Entry(wrapper3, textvariable=t13)
ent13.grid(row=2, column=5, padx=5, pady=6)
print("-------------------data entry end-------------------------")


add_btn = Button(wrapper3, text="Add New", bg="black", fg="white", command=add_new)
# add_btn.pack(side=tk.RIGHT)
add_btn.grid(row=4, column=5, sticky=tk.W+tk.E)
# add_btn.grid(row=7, column=0, padx=5, pady=3, side=tk.RIGHT)

root.title("Stock Data Management Application")
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.mainloop()

