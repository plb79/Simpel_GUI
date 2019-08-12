import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter.scrolledtext import *
from tkinter import messagebox

#Structure and  Layout
window = Tk()
window.title("Simpel GUI")
window.geometry("750x450")

style = ttk.Style(window)
style.configure("lefttab.TNotebook", tabposition='wn')

# Tab layaout
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

# Add tabs to notebook
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"View":^20s}')
tab_control.add(tab3, text=f'{"Search":^20s}')
tab_control.add(tab4, text=f'{"Export":^20s}')
tab_control.add(tab5, text=f'{"About":^20s}')

tab_control.pack(expand=2, fill="both")

label1 = Label(tab1, text="Simple GUI", padx=5, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text="View", padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text="Search", padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab4, text="Export", padx=5, pady=5)
label4.grid(column=0, row=0)

label5 = Label(tab5, text="About", padx=5, pady=5)
label5.grid(column=0, row=0)

# Information Tabs Rightside

# Main Home
l1 = Label(tab1, text="First Name", padx=5, pady=5)
l1.grid(column=0, row=1)
fname_raw_entry = StringVar()
entry_fname = Entry(tab1, textvariable=fname_raw_entry, width=50)
entry_fname.grid(row=1, column=1)

l2 = Label(tab1, text="Last Name", padx=5, pady=5)
l2.grid(column=0, row=2)
lname_raw_entry = StringVar()
entry_lname = Entry(tab1, textvariable=lname_raw_entry, width=50)
entry_lname.grid(row=2, column=1)

l3 = Label(tab1, text="Email", padx=5, pady=5)
l3.grid(column=0, row=3)
email_raw_entry = StringVar()
entry_email = Entry(tab1, textvariable=email_raw_entry, width=50)
entry_email.grid(row=3, column=1)

l4 = Label(tab1, text="Age", padx=5, pady=5)
l4.grid(column=0, row=4)
age_raw_entry = IntVar()
entry_age = Entry(tab1, textvariable=age_raw_entry, width=50)
entry_age.grid(row=4, column=1)

l5 = Label(tab1, text="Date of Birth", padx=5, pady=5)
l5.grid(column=0, row=5)
dob_raw_entry = StringVar()
cal = DateEntry(tab1,  width=30, textvariable=dob_raw_entry,
                background='darkblue', foreground='white', borderwidth=2, year=2019)
cal.grid(row=5, column=1, padx=10, pady=10)

l6 = Label(tab1, text="Adress", padx=5, pady=5)
l6.grid(column=0, row=6)
adress_raw_entry = StringVar()
entry_adress = Entry(tab1, textvariable=adress_raw_entry, width=50)
entry_adress.grid(row=6, column=1)

l7 = Label(tab1, text="Phone Number", padx=5, pady=5)
l7.grid(column=0, row=7)
pnumber_raw_entry = IntVar()
entry_pnumber = Entry(tab1, textvariable=pnumber_raw_entry, width=50)
entry_pnumber.grid(row=7, column=1)

Btn1 = Button(tab1, text="Add", width=12, bg="#03A9F4", fg="#fff")
Btn1.grid(row=8, column=0, padx=5, pady=5)

Btn2 = Button(tab1, text="Clear", width=12, bg="#03A9F4", fg="#fff")
Btn2.grid(row=8, column=1, padx=5, pady=5)

# Display Screen

tab1_display = ScrolledText(tab1, height=5)
tab1_display.grid(row=10, column=1, padx=5, pady=5, columnspan=3)

Btn3 = Button(tab1, text="Clear Result", width=12, bg="#03A9F4", fg="#fff")
Btn3.grid(row=12, column=1, padx=10, pady=10)
# View

# Search

# Export

# About


window.mainloop()
