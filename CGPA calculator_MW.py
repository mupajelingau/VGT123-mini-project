from tkinter import *

#creating main window
root = Tk()
root.title("Welcome to CGPA CALCULATOR!")
root.geometry("600x400")

label_1 = Label (root, text = "NAME", fg="blue", bg="pink", font="Arial 12 bold italic")
label_2 = Label (root, text = "NO. MATRIC", fg="blue", bg="pink", font="Arial 12 bold italic")
label_3 = Label (root, text = "PASSWORD", fg="blue", bg="pink", font="Arial 12 bold italic")
entry_1 = Entry (root)
entry_2 = Entry (root)
entry_3 = Entry (root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
label_3.grid(row=2, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)

#create button
buttonSave= Button(root, text="Save")
buttonSave.grid(column=0)

buttonClear= Button(root, text="Clear")
buttonClear.grid(row=3, column=1)

buttonExit= Button(root, text="Exit")
buttonExit.grid(row=3, column=2)


#call main loop
root.mainloop()
