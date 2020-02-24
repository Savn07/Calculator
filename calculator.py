from tkinter import *

expression = "" 

def press(num): 
            global expression 
            expression = expression + str(num) 
            equation.set(expression) 

def equalpress(): 
	
        try:
            global expression
            total = str(eval(expression)) 
            equation.set(total) 
            expression = ""
        except: 
            equation.set(" error ") 
            expression = "" 

def clear(): 
	global expression 
	expression = "" 
	equation.set("") 

if __name__ == "__main__": 
	gui = Tk() 
	gui.configure(background="light green") 
	gui.title("Simple Calculator") 
	gui.geometry("790x433") 
	equation = StringVar() 
	expression_field = Entry(gui, textvariable=equation,font=('arial', 16)) 
	expression_field.grid(columnspan=10, ipadx=280,ipady=17)
	
	equation.set('Enter your expression') 
 
	button1 = Button(gui, text=' 1 ',font=('arial', 16,'bold'), fg='black', bg='red', 
					command=lambda: press(1), height=3, width=14) 
	button1.grid(row=2, column=0) 

	button2 = Button(gui, text=' 2 ', font=('arial', 16,'bold'),fg='black', bg='red', 
					command=lambda: press(2), height=3, width=14) 
	button2.grid(row=2, column=1) 

	button3 = Button(gui, text=' 3 ', font=('arial', 16,'bold'),fg='black', bg='red', 
					command=lambda: press(3), height=3, width=14) 
	button3.grid(row=2, column=2) 

	button4 = Button(gui, text=' 4 ', font=('arial', 16,'bold'),fg='black', bg='red', 
					command=lambda: press(4), height=3, width=14) 
	button4.grid(row=3, column=0) 

	button5 = Button(gui, text=' 5 ',font=('arial', 16,'bold'), fg='black', bg='red', 
					command=lambda: press(5), height=3, width=14) 
	button5.grid(row=3, column=1) 

	button6 = Button(gui, text=' 6 ',font=('arial', 16,'bold'), fg='black', bg='red', 
					command=lambda: press(6), height=3, width=14) 
	button6.grid(row=3, column=2) 

	button7 = Button(gui, text=' 7 ',font=('arial', 16,'bold'), fg='black', bg='red', 
					command=lambda: press(7), height=3, width=14) 
	button7.grid(row=4, column=0) 

	button8 = Button(gui, text=' 8 ',font=('arial', 16,'bold'), fg='black', bg='red', 
					command=lambda: press(8), height=3, width=14) 
	button8.grid(row=4, column=1) 

	button9 = Button(gui, text=' 9 ',font=('arial', 16,'bold'), fg='black', bg='red', 
					command=lambda: press(9), height=3, width=14) 
	button9.grid(row=4, column=2) 

	button0 = Button(gui, text=' 0 ', font=('arial', 16,'bold'),fg='black', bg='red', 
					command=lambda: press(0), height=3, width=14) 
	button0.grid(row=5, column=0) 

	plus = Button(gui, text=' + ', font=('arial', 16,'bold'),fg='black', bg='red', 
				command=lambda: press("+"), height=3, width=14) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ',font=('arial', 16,'bold'), fg='black', bg='red', 
				command=lambda: press("-"), height=3, width=14) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' * ',font=('arial', 16,'bold'), fg='black', bg='red', 
					command=lambda: press("*"), height=3, width=14) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ',font=('arial', 16,'bold'), fg='black', bg='red', 
					command=lambda: press("/"), height=3, width=14) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' = ', font=('arial', 16,'bold'),fg='black', bg='red', 
				command=equalpress, height=3, width=14) 
	equal.grid(row=5, column=2) 

	clear = Button(gui, text='Clear',font=('arial', 16,'bold'), fg='black', bg='red', 
				command=clear, height=3, width=14) 
	clear.grid(row=5, column='1') 

	gui.mainloop() 
