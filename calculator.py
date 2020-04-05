from tkinter import*
def btnClick(numbers):
    global operator
    operator=operator+ str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
cal=Tk()
cal.title("calculator")
operator=""
text_Input =StringVar()
txtDisplay = Entry(cal,font=('arial',20,'bold') , textvariable=text_Input, bd=30, insertwidth=4, bg="light blue", justify='right').grid(columnspan=4)
btn7=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="7",command=lambda:btnClick(7),bg="light blue").grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="8",command=lambda:btnClick(8),bg="light blue").grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="9",command=lambda:btnClick(9),bg="light blue").grid(row=1,column=2)
add=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="+",command=lambda:btnClick("+"),bg="light blue").grid(row=1,column=3)
#=================================================================================================================
btn4=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="4",command=lambda:btnClick(4),bg="powder blue").grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="5",command=lambda:btnClick(5),bg="light blue").grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="6",command=lambda:btnClick(6),bg="light blue").grid(row=2,column=2)
sub=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="-",command=lambda:btnClick("-"),bg="light blue").grid(row=2,column=3)
#=================================================================================================================
btn1=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="1",command=lambda:btnClick(1),bg="light blue").grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="2",command=lambda:btnClick(2),bg="light blue").grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="3",command=lambda:btnClick(3),bg="light blue").grid(row=3,column=2)
mul=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="*",command=lambda:btnClick("*"),bg="light blue").grid(row=3,column=3)
#==================================================================================================================
btn0=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="0",command=lambda:btnClick(0),bg="light blue").grid(row=4,column=0)
btnclr=Button(cal,padx=14,bd=8,fg="black",font=('árial',20,'bold'),text="C",bg="light blue",command=btnClearDisplay).grid(row=4,column=1)
btneq=Button(cal,padx=18,bd=8,fg="black",font=('árial',20,'bold'),text="=",bg="light blue",command=btnEqualsInput).grid(row=4,column=3)
div=Button(cal,padx=16,bd=8,fg="black",font=('árial',20,'bold'),text="/",command=lambda:btnClick("/"),bg="light blue").grid(row=4,column=2)




cal.mainloop()
