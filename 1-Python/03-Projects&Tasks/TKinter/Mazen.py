from tkinter import *
import os
os.system("cls")

i = 0

def Func():
    global i
    i += 1
    print("Spectre tamer")
    
def count():
	
    print(int(i))

	
window_1 = Tk()
window_1.geometry('1000x500')
window_1.title("Hello Tkinter")
window_1.configure(bg='lightgray')

label_1 = Label(window_1, text="Mazen", fg='blue', bg='green')
label_1.pack(side=TOP)

B_1 = Button(window_1, text="Counter", bd=10, command=count, fg='yellow', bg='green')
B_1.pack(side=BOTTOM)

photo_1 = PhotoImage(file='iti.png')
photo_1 = photo_1.subsample(1, 1)

B_2 = Button(window_1, text="Turn Off", bd=10, image=photo_1, command=Func, bg='lightblue')
B_2.place(x=450, y=200, anchor=CENTER)

window_1.mainloop()
