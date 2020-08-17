
#creating main window
root = Tk()
root.title("CGPA CALCULATOR")

label_1 = Label (root, text = "NAME")
label_2 = Label (root, text = "NO. MATRIC")
label_3 = Label (root, text = "PASSWORD")
entry_1 = Entry (root)
entry_2 = Entry (root)
entry_3 = Entry (root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
label_3.grid(row=2, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)

root.mainloop()
