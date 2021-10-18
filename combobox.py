import tkinter as tk
import tkinter.ttk as ttk

main= tk.Tk()
main.title("hef")
main.geometry("400x400")
def get_val(jjh):
    print(combobox1.get())

combobox1=ttk.Combobox(main, value=["Sifat", "Raktim", "Anik", "Pranto", "Ahad"])
combobox1.bind("<<ComboboxSelected>>", get_val)
combobox1.pack()

main.mainloop()