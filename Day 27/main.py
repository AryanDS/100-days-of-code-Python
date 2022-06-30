import _tkinter
from  tkinter import *

from debugpy import listen

#Creating a new object
window = Tk()

window.title("My first GUI program")
#Defining the minimum size of the window, it can be more if needed but would not be below this.
window.minsize(width=500, height=400)


#Label
#will create a label object
my_label = Label(text ="My Label", font=("Arial", 24, "bold"))

#below will make sure that the label is on screen, packer to pack the label onscreen
#Will also help in placing the label in the GUI screen, if there is no pack then there is no label placed!
# my_label.pack()
#place will help with the positioning of the object and it is very specific! based on x,y
# my_label.place(x=0,y=0)

#best to use , relative to other components, based on row and columns!
my_label.grid(column=0,row=0)

#Cannot mix pack and grid!

#Changing the text in the my_label object
my_label["text"]="New text but CR7 is the greatest!"

#Another method to do the same thing below:
my_label.config(text="Another check but SIIIIIIIUUUU")


def button_clicked():
    print("The button was clicked!")
    my_text= entry.get()
    my_label.config(text=my_text)

#Buttom
button = Button(text="Click ME", command=button_clicked)
button.grid(column=1,row=1)



def button_clicked2():
    print("The button was clicked!")
    # my_text= entry.get()
    # my_label.config(text=my_text)

#Buttom
button2 = Button(text="Click ME", command=button_clicked2)
button2.grid(column=2, row=1)


#Entry 
entry = Entry(width=10)
entry.insert(END, string="Begin with something")
print(entry.get())

entry.grid(column=4,row=4)


# #Text BOX
# text = Text(height=5, width=30)
# #Below will ensure that the cursor is in the text box
# text.focus()
# #Will add text to the text box
# text.insert(END, "Example of multi-line entry")
# text.pack()


# #Spinbox
# def spinbox_used():
#     print(spinbox.get())

# spinbox = Spinbox(from_=0, to=7, width=5, command=spinbox_used)
# spinbox.pack()


# #Scale
# #the function call will pass the value that the user uses in the GUI
# def Scale_used(value):
#     print(value)

# scale = Scale(from_=0, to=77, command=Scale_used)
# scale.pack()



# #Check button
# def checkbutton_used():
#     #will print 1 for checked button else 0
#     print(checked_state.get())

# checked_state=IntVar()
# checkbutton =  Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()

# #Radio button
# def radio_used():
#     print(radio_state.get())


# radio_state= IntVar()

# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

# radiobutton1.pack()
# radiobutton2.pack()


# #Listen box
# def listbox_used():
#     print(listbox.get(listbox.curselection()))

# listbox= Listbox(width=5,height=3)
# fruits=["Apple","Banana","Orange","Grape"]
# for fruit in fruits:
#     listbox.insert(fruits.index(fruit), fruit)

# listbox.bind("<<ListenboxSelect>>", listbox_used)    
# listbox.pack()


#Will keep the window running 
window.mainloop()