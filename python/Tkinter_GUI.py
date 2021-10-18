import tkinter as gui

main=gui.Tk()
main.title("Sifat's")
main.geometry("625x461")
main.minsize(400,200)

label=gui.Label(main, text="tKinter Boss",
                bg="grey", fg="yellow", padx=800,
                pady=10, font="comicsansms 20 bold")
label.pack()
photo=gui.PhotoImage(file="img.png")
label1=gui.Label(image=photo)
label1.pack()

main.mainloop()