from tkinter import *

from pyparsing import col


#Creating a new object
window = Tk()

window.title("My first GUI program")
#Defining the minimum size of the window, it can be more if needed but would not be below this.
window.minsize(width=500, height=400)

def result_convertor():
    miles = entry.get()
    km = 1.6 * int(miles)
    result.config(text=km)

#lets set the layout first

#Entry 
entry = Entry(width=10)
entry.insert(END, string="0")
print(entry.get())

entry.grid(column=1,row=0)


#adding miles label 
miles = Label(text ="Miles", font=("Arial", 24, "bold"))
miles.grid(column=2,row=0)


#adding is equal to  label 
is_equal_to = Label(text ="is equal to", font=("Arial", 24, "bold"))
miles.grid(column=0,row=1)


#result label
result =  Label(text=0, font=("Arial", 24, "bold"))
result.grid(column=1,row=1)


#adding KM label 
km = Label(text ="KM", font=("Arial", 24, "bold"))
km.grid(column=2,row=1)


#Calculate button 
def call_result():
    result_convertor()
    
#Buttom
button = Button(text="Calculate", command=call_result)
button.grid(column=1,row=2)


#Will keep the window running 
window.mainloop()