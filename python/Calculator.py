import tkinter as tk

main_win = tk.Tk()
main_win.title("Sifat's Calculator")
main_win.geometry("400x400")
main_win.maxsize(600, 600)

expression = ""

def keys(key):
    global expression
    expression= expression + str(key)
    inputxt.set(expression)

def key_clr():
    global expression
    expression = " "
    inputxt.set(expression)

def key_eq():
    equal=eval(expression)
    inputxt.set(equal)

inputxt=tk.StringVar()

#expression field
exps_field=tk.Entry(main_win,font="arial 16 bold",justify="right", textvariable=inputxt)
exps_field.grid(row=0, column=1, columnspan=4,ipadx=20,ipady=15)
#buttons
button1=tk.Button(main_win, text="1",height=3,width=8, command=lambda:keys("1"))
button1.grid(row=2, column=1,sticky="nsew")
button2=tk.Button(main_win, text="2",height=3,width=8, command=lambda:keys("2"))
button2.grid(row=2, column=2,sticky="nsew")
button3=tk.Button(main_win, text="3",height=3,width=8, command=lambda:keys("3"))
button3.grid(row=2, column=3,sticky="nsew")
button4=tk.Button(main_win, text="4",height=3,width=8, command=lambda:keys("4"))
button4.grid(row=3, column=1,sticky="nsew")
button5=tk.Button(main_win, text="5",height=3,width=8, command=lambda:keys("5"))
button5.grid(row=3, column=2,sticky="nsew")
button6=tk.Button(main_win, text="6",height=3,width=8, command=lambda:keys("6"))
button6.grid(row=3, column=3,sticky="nsew")
button7=tk.Button(main_win, text="7",height=3,width=8, command=lambda:keys("7"))
button7.grid(row=4, column=1,sticky="nsew")
button8=tk.Button(main_win, text="8",height=3,width=8, command=lambda:keys("8"))
button8.grid(row=4, column=2,sticky="nsew")
button9=tk.Button(main_win, text="9",height=3,width=8, command=lambda:keys("9"))
button9.grid(row=4, column=3,sticky="nsew")
button0=tk.Button(main_win, text="0",height=3,width=8, command=lambda:keys("0"))
button0.grid(row=5, column=1,sticky="nsew")

buttonclr=tk.Button(main_win, text="clr",height=3,width=8, command=key_clr)
buttonclr.grid(row=5, column=2,sticky="nsew")
buttoneq=tk.Button(main_win, text="=",height=3,width=8, command=key_eq)
buttoneq.grid(row=5, column=3,sticky="nsew")

buttonpls=tk.Button(main_win, text="+",height=3,width=8, command=lambda:keys("+"))
buttonpls.grid(row=2, column=4,sticky="nsew")
buttonsub=tk.Button(main_win, text="-",height=3,width=8, command=lambda:keys("-"))
buttonsub.grid(row=3, column=4,sticky="nsew")
buttonmul=tk.Button(main_win, text="*",height=3,width=8, command=lambda:keys("*"))
buttonmul.grid(row=4, column=4,sticky="nsew")
buttondiv=tk.Button(main_win, text="/",height=3,width=8, command=lambda:keys("/"))
buttondiv.grid(row=5, column=4,sticky="nsew")

main_win.mainloop()
