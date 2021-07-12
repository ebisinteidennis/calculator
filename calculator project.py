from tkinter import*

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqualsinput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

cal =Tk()
cal.title("ebisintei calculator")
operator =""
text_input =StringVar()
cal.geometry = ("100x100")


txtDisplay = Entry(cal,font =("Chiller", 20,"bold"), textvariable = text_input, bd=20,
                   insertwidth=1, bg="red",justify="right").grid(columnspan=4,rowspan=1)

btn7=Button(cal,padx=8, pady=8, bd=8, fg="black",font=("Chiller", 20, "bold"),text="7",
            bg="red",command=lambda:btnClick(7)).grid(row=1,column=0)

btn8=Button(cal,padx=8, pady=8, bd=8, fg="black",font=("Chiller", 20, "bold"),
            text="8", bg="red",command=lambda:btnClick(8)).grid(row=1,column=1)

btn9=Button(cal,padx=8,pady=8, bd=8, fg="black",font=("Chiller", 20, "bold"),
            text="9", bg="red", command=lambda :btnClick(9)).grid(row=1,column=2)

Addition= Button(cal,padx=8, pady=8, bd=8, fg="black", font=("Chiller", 20, "bold" ),text="+",
                 bg="red", command=lambda:btnClick('+')).grid(row=1, column=3)

#======================================================================================

btn4=Button(cal,padx=8,pady=8, bd=8, fg="black",font=("Chiller", 20, "bold"),
            text="4", bg="red", command=lambda :btnClick(4)).grid(row=2,column=0)

btn5=Button(cal,padx=8, pady=8, bd=8, fg="black",font=("Chiller", 20, "bold"),
            text="5", bg="red",command=lambda:btnClick(5)).grid(row=2,column=1)

btn6=Button(cal,padx=8,pady=8, bd=8, fg="black",font=("Chiller", 20, "bold"),
            text="6", bg="red",command=lambda :btnClick(6)).grid(row=2,column=2)

subtraction= Button(cal,padx=8, pady=8, bd=8, fg="black", font=("Chiller", 20, "bold" ),
                    text="-", bg="red", command=lambda:btnClick('-')).grid(row=2, column=3)

#==================================================================================

btn1=Button(cal,padx=8, pady= 8,bd=8, fg="black",font=("Chiller", 20, "bold"),
            text="1", bg="red", command=lambda:btnClick(1)).grid(row=3,column=0)

btn2=Button(cal,padx=8, pady=8, bd=8, fg="black",font=("Chiller", 20, "bold"),
            text="2", bg="red", command=lambda:btnClick(2)).grid(row=3,column=1)

btn3=Button(cal,padx=8, pady=8, bd=8, fg="black",font=("Chiller", 20, "bold"),
            text="3", bg="red", command=lambda:btnClick(3)).grid(row=3,column=2)

Multiplication= Button(cal,padx=8, pady=8, bd=8, fg="black", font=("Chiller", 20, "bold" ),
                       text="*", bg="red", command=lambda:btnClick('*')).grid(row=3, column=3)

#==================================================================================

btn0=Button(cal,padx=8 ,pady=8, bd=8, fg="black",font=("Chiller", 20, "bold"),
            text="0", bg="red",command=lambda:btnClick(0)).grid(row=4,column=0)

btnClear=Button(cal,padx=8, pady=8, bd=8, fg="black",font=("chiller", 20, "bold"),
                text="C", bg="red", command=btnClearDisplay).grid(row=4,column=1)

btnEquals=Button(cal,padx=8, pady=8, bd=8 , fg="black",font=("Chiller", 20, "bold"),
                 text="=", bg="red", command=btnEqualsinput).grid(row=4,column=2)

Division= Button(cal,padx=8, pady=8, bd=8, fg="black", font=("Chiller", 20, "bold" ),
                 text="/", bg="red", command=lambda:btnClick('/')).grid(row=4, column=3)


cal.mainloop()
