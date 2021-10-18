import tkinter as tk

main=tk.Tk()
main.title("Sifat's")
main.geometry("625x461")
main.minsize(400, 200)
#password input method
username_label=tk.Label(main,text="Enter Username :", font="comicsansms 10 bold")
password_label=tk.Label(main, text="Enter Password :", font="comicsansms 10 bold")
username_label.grid(row=2, column=2)
password_label.grid(row=3, column=2)

#entry
username_entry=tk.Entry(main)
password_entry=tk.Entry(main)
username_entry.grid(row=2,column=3)
password_entry.grid(row=3,column=3)

#submit button
def get_value():
    print("Username :", username_entry.get())
    print("Password :", password_entry.get())

submit_button= tk.Button(text="Submit",command=get_value)
submit_button.grid(row=4, column=3)

main.mainloop()