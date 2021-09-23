from tkinter import *
from tkinter.messagebox import *
import History.num_history


# important functions
def key_board_click():
    buttonFrame = textField.get()
    print(buttonFrame)


def clear():
    ex = textField.get()
    ex = ex[0:len(ex) - 2]
    textField.delete(0, END)
    textField.insert(0, ex)


def all_clear():
    textField.delete(0, END)


font = ("verdana", 12, "bold")


def click_button_function(event):
    #print("Clicked",end='')
    b = event.widget
    text = b['text']
    print(text)

    if text == "=":
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            print("Error..", e)
            showerror("Error", e)
        return
    textField.insert(END, text)


# create a window
cal = Tk()
cal.title("Calculator")
cal.geometry("300x370")
cal.wm_iconbitmap("cal3.ico")

# picture label
pic = PhotoImage(file="logofor.png")
headingLabel = Label(cal, image=pic)
headingLabel.pack(side=TOP, pady=10)

# heading label
heading = Label(cal, text="Dennis Ebisintei", font=font, underline=1)
heading.pack(side=TOP)

# text field
textField = Entry(cal, font=font, justify=CENTER)
textField.pack(side=TOP, pady=10, fill=X, padx=10)

# buttons
buttonFrame = Frame(cal)
buttonFrame.pack(side=TOP, pady=10)

# adding buttons
temp = 1
for i in range(0, 3):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief="ridge", activebackground="blue",
                     activeforeground="white")
        btn.grid(row=i, column=j)
        temp = temp + 1
        btn.bind("<Button-1>", click_button_function)

zerobtn = Button(buttonFrame, text="0", font=font, width=5, relief="ridge", activebackground="blue")
zerobtn.grid(row=3, column=0)

dotbtn = Button(buttonFrame, text=".", font=font, width=5, relief="ridge", activebackground="blue")
dotbtn.grid(row=3, column=1)

equalbtn = Button(buttonFrame, text="=", font=font, width=5, relief="ridge", activebackground="blue")
equalbtn.grid(row=3, column=2)

plusBtn = Button(buttonFrame, text="+", font=font, width=5, relief="ridge", activebackground="blue")
plusBtn.grid(row=0, column=3)

SubtractBtn = Button(buttonFrame, text="-", font=font, width=5, relief="ridge", activebackground="blue")
SubtractBtn.grid(row=1, column=3)

mulBtn = Button(buttonFrame, text="*", font=font, width=5, relief="ridge", activebackground="blue")
mulBtn.grid(row=2, column=3)

divideBtn = Button(buttonFrame, text="/", font=font, width=5, relief="ridge", activebackground="blue")
divideBtn.grid(row=3, column=3)

clearBtn = Button(buttonFrame, text="C", font=font, width=11, relief="ridge", activebackground="blue", command=clear)
clearBtn.grid(row=4, column=0, padx=3, pady=3, columnspan=2)

allclearBtn = Button(buttonFrame, text="AC", font=font, width=11, relief="ridge", activebackground="blue",
                     command=all_clear)
allclearBtn.grid(row=4, column=2, padx=3, pady=3, columnspan=2)

# binding all buttons
zerobtn.bind("<Button-1>", click_button_function)
dotbtn.bind("<Button-1>", click_button_function)
equalbtn.bind("<Button-1>", click_button_function)
plusBtn.bind("<Button-1>", click_button_function)
mulBtn.bind("<Button-1>", click_button_function)
divideBtn.bind("<Button-1>", click_button_function)
clearBtn.bind("<Button-1>", click_button_function)
allclearBtn.bind("<Button-1>", click_button_function)
SubtractBtn.bind("<Button-1>", click_button_function)

cal.mainloop()
