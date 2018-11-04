from tkinter import *

import script1


def word_search():
    meaning = script1.search(word.get())
    list1.delete(0, END)
    for row in meaning:
        list1.insert(END, row)


window = Tk()

window.wm_title("Dictionary_by_Nikhil")

word = StringVar()
e1 = Entry(window, textvar=word, width=100)
e1.grid(row=0, columnspan=35)

b1 = Button(window, text="Search", command=word_search)
b1.grid(row=1, columnspan=7)

list1 = Listbox(window, height=20, width=100)
list1.grid(row=3, column=0)

window.mainloop()
