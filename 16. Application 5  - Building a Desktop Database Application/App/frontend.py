from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e.delete(0,END)
    e.insert(END,selected_tuple[1])
    e1.delete(0,END)
    e1.insert(END,selected_tuple[2])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[3])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
        
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,{title_text.get(),author_text.get(),year_text.get(),isbn_text.get()})

def delete_command():
    backend.delete(selected_tuple[0])
    
def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        
window=Tk()

window.wm_title("Book Store")

## GUI for Table, Author, Year, ISBN entries    
    
a=Label(window,text="Title")
a.grid(row=0,column=0)

title_text=StringVar()
e=Entry(window,textvariable=title_text)
e.grid(row=0,column=1)

a1=Label(window,text="Author")
a1.grid(row=0,column=2)

author_text=StringVar()
e1=Entry(window,textvariable=author_text)
e1.grid(row=0,column=3)

a2=Label(window,text="Year")
a2.grid(row=1,column=0)

year_text=StringVar()
e2=Entry(window,textvariable=year_text)
e2.grid(row=1,column=1)

a3=Label(window,text="ISBN")
a3.grid(row=1,column=2)

isbn_text=StringVar()
e3=Entry(window,textvariable=isbn_text)
e3.grid(row=1,column=3)

## GUI for List Box and Scrollbar

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb=Scrollbar(window)
sb.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

## GUI for Buttons (View all, Search entry, Add entry, delete, update and close)

b=Button(window,text="View all",width=12,command=view_command)
b.grid(row=2,column=3)

b1=Button(window,text="Search entry",width=12,command=search_command)
b1.grid(row=3,column=3)

b2=Button(window,text="Add entry",width=12,command=add_command)
b2.grid(row=4,column=3)

b3=Button(window,text="Update selected",width=12,command=update_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Delete selected",width=12,command=delete_command)
b4.grid(row=6,column=3)

b5=Button(window,text="Close",width=12,command=window.destroy)
b5.grid(row=7,column=3)

window.mainloop()
