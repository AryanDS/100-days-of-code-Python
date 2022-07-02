
import email
from tkinter import *
from turtle import width
import random 
from pyparsing import col
FONT_NAME = "Courier"
from matplotlib import image
import os
from tkinter import messagebox
import pyperclip
import json
"""
If you are creating a file and want the file to be created with the subdirectory,
You would need to change the directory using the below commands
import os
print(os.getcwd())
os.chdir('path')

"""

#Changing the working directory 
os.chdir("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 29")

#checking whether the directory was changed
print(os.getcwd())
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letter=[random.choice(letters) for char in range(nr_letters)]
    password_symbol=[random.choice(symbols) for char in range(nr_symbols)]
    password_number=[random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number

    random.shuffle(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    #pythonic way 
    password = "".join(password_list)
    pyperclip.copy(password)
    pass_website.insert(0, password)
    
   

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_entry = text_website.get()
    email_entry = email_website.get()
    pass_entry =  pass_website.get()

    #Creating a dictionary 
    new_data = {
        website_entry:{
            "email": email_entry,
            "password": pass_entry
        }
        
    }
    # file.write(f"{website_entry} | {email_entry} | {pass_entry}\n")
    """
    json.dump will write the data into a json file and using "w" we are able to create a
    json file if it does not exists.
    """
    #json.dump(new_data, file, indent=4)
    """
    json.load will load the json file and we can print it in the console, "r" use this to do so.
    """
    # data = json.load(file)
   # print(data)

    #Below will read the json file, update the json file with the new data and then append to the existing data.


    #Creating a message box 
    #messagebox.showinfo(title=" ", message =" ")
    #the output from the below method call is a boolean
    # if len(website_entry) or len(pass_entry) == 0:
    #         messagebox.showinfo(title="Oops", message="The field is empty, Please try again!")
    # else:        
        # message_output = messagebox.askokcancel(title=website_entry, message=f"These are the new details entered Email: {email_entry}"
        # f" \n Password: {pass_entry} \n Is it okay to save?")

        # if message_output:
    try:    #fetching all the data from the ENTRY BOX
        with open("pass_data.json", "r") as data_file:
            #Reading the old data
            data = json.load(data_file)

    except FileNotFoundError:
        with open("pass_data.json","w") as data_file:
            json.dump(new_data, data_file, indent=4)
            #updating the old data with the new data.
            #It will add another entry into the same dictionary or JSON 
    else:
        data.update(new_data)

        with open("pass_data.json","w") as data_file:
                json.dump(data, data_file, indent=4)    

    finally:      
          #Below will ensure that after clicking on add the contents are deleted for a new entry.
            text_website.delete(0, END)
            pass_website.delete(0,END)
    



def find_password():
    """
    find whether the user website is in the json file or not 
    """
    #catching user input of the website to be searched
    website_entry = text_website.get()
    try:
        with open("pass_data.json", "r") as data_file:
            #loading the JSON object into a dictionary 
            json_dict =  json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error ", message="The file does not exists!.")
           #looping through the json file keys 
    else:       
        print(json_dict.keys())
        for key in json_dict.keys():
            if website_entry == key:
                #print(website_entry, key)
                messagebox.showinfo(title=f"{website_entry}", message=f"Email: {json_dict[key]['email']} \n Password: {json_dict[key]['password']}")
                break
            else:
                messagebox.showinfo(title="Oops", message="Data not found!") 
        messagebox.showinfo(title=f"{website_entry}", message=f"Email: {json_dict[key]['email']} \n Password: {json_dict[key]['password']}") if website_entry in json_dict else messagebox.showinfo(title="Oops", message="Data not found!") 

# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

pass_logo= PhotoImage(file="/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 29/password-manager-start/logo.png")

canvas = Canvas(width =200, height=200, bg="white")
canvas.create_image(100, 100, image=pass_logo)
canvas.grid(column=1,row=0)




#creating labels
website = Label(text ="Website: ",  font=(FONT_NAME, 11, "bold"))
website.grid(column=0,row=1)

email_username = Label(text ="Email/ Username:",  font=(FONT_NAME, 11, "bold"))
email_username.grid(column=0,row=2)


password =Label(text ="Password:",  font=(FONT_NAME, 11, "bold"))
password.grid(column=0,row=3)


#Creating Entry box

text_website = Entry(width=35)
text_website.grid(column=1, row=1)
text_website.focus()




email_website = Entry(width=35)
email_website.grid(column=1, row=2, columnspan=2)
email_website.insert(0,"aryansaini117@gmail.com")

pass_website = Entry(width=21)
pass_website.grid(column=1, row=3)


#Creating buttons 


#Buttom Generate
button_pass = Button(text="Generate Password", command=generate_password)
button_pass.grid(column=2, row=3)


#Buttom Generate
button_add = Button(text="Add", command=save, width=36)
button_add.grid(column=1, row=4, columnspan=2)

#Search buttom
search_but = Button(text="Search", command= find_password)
search_but.grid(column=2, row=1)

window.mainloop()