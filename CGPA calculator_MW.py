from tkinter import *
import sqlite3

#function for saveButton
def saveButton():
    print("Saving data...")

    conn = sqlite3.connect("cgpaCalculator.db")

    c = conn.cursor()

    c.execute("INSERT INTO personal (name, matric, program, ic, phone, email) VALUES (?, ?, ?, ?, ?, ?)",
            (entry_name.get(), entry_matric.get(), entry_prgm.get(), entry_ic.get(), entry_ph.get(), entry_email.get(),))

    conn.commit()

    conn.close()

#function for clearButton
def clearButton():
    entry_name.delete(0,END)
    entry_matric.delete(0,END)
    entry_prgm.delete(0,END)
    entry_ic.delete(0,END)
    entry_ph.delete(0,END)
    entry_email.delete(0,END)

#function for exitButton
def exitButton():
    root.destroy()

#function open new window
def openNew_window():
    new_win = Toplevel(root)
    new_win.geometry("300x200")
    lbl_cgpa = Label(new_win, text= "HI! WELCOME TO CGPA CALCULATOR", fg="black", font="Arial 11 bold italic")
    lbl_cgpa.grid()
    
    #button in new window
    buttonExit= Button(new_win, text="Exit", width=6, command= exitButton)
    buttonExit.grid()

#creating main window
root = Tk()
root.title("CGPA CALCULATOR")
root.geometry("550x255")


label_title = Label (root, text = "CGPA CALCULATOR", fg="black", font="Arial 11 bold italic")
label_title.grid(row=0)
frame1 = LabelFrame(root, padx=40, pady=40, text= "Personal Information", bg="white", font= "Arial 11 bold")
frame1.grid()
label_name = Label (frame1, text = "NAME", fg="blue", bg="white", font="Arial 11 bold italic")
label_matric = Label (frame1, text = "NO. MATRIC", fg="blue", bg="white", font="Arial 11 bold italic")
label_prgm = Label (frame1, text = "PROGRAMME", fg="blue", bg="white", font="Arial 11 bold italic")
label_ic = Label (frame1, text = "IC NUMBER", fg="blue", bg="white", font="Arial 11 bold italic")
label_ph = Label (frame1, text = "PHONE NUMBER", fg="blue", bg="white", font="Arial 11 bold italic")
label_email = Label (frame1, text = "EMAIL", fg="blue", bg="white", font="Arial 11 bold italic")


entry_name = Entry (frame1, width=40)
entry_matric  = Entry (frame1, width=40)
entry_prgm  = Entry (frame1, width=40)
entry_ic = Entry (frame1, width=40)
entry_ph = Entry (frame1, width=40)
entry_email = Entry (frame1, width=40)

label_name.grid(row=1, sticky=W)
label_matric.grid(row=2, sticky=W)
label_prgm.grid(row=3, sticky=W)
label_ic.grid(row=4, sticky=W)
label_ph.grid(row=5, sticky=W)
label_email.grid(row=6, sticky=W)

entry_name.grid(row=1, column=1)
entry_matric.grid(row=2, column=1)
entry_prgm.grid(row=3, column=1)
entry_ic.grid(row=4, column=1)
entry_ph.grid(row=5, column=1)
entry_email.grid(row=6, column=1)

#create button
buttonSave= Button(frame1, text="Save", width=10, command= saveButton)
buttonSave.grid(row=7)

buttonClear= Button(frame1, text="Clear All", width=10, command= clearButton)
buttonClear.grid(row=7, column=1)

buttonNext= Button(frame1, text="Next>>", width=10, command= openNew_window)
buttonNext.grid(row=7, column=2)



#call main loop
root.mainloop()