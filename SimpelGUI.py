import tkinter as tk
from tkinter import *
from tkinter import ttk

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

# View

# Search

# Export

# About


window.mainloop()
