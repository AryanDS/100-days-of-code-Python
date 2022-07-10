##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
# 1. Update the birthdays.csv
data = pd.read_csv("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 32/birthday-wisher-extrahard-start/birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv

#getting todays date
now = dt.datetime.now()
month = now.month
day =  now.day

#checking if the month and day matches any of the data in the csv file.
data_month = data["month"]
data_day = data["day"]   

print(data_month)
print(data_day)


for i, j in zip(data_month, data_day):
    if i == month and j == day:
        send_email= True
        #using the loc() to get the name 
        person_name = data.loc(data["month"]== i and data["day"] == j, "name" ).item()
        

print(send_email)
print(person_name)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
list_files = []

with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 32/birthday-wisher-extrahard-start/letter_templates/letter_1.txt") as file:
    file1 = [line.strip() for line in file.readlines()]

list_files.append(file1)

with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 32/birthday-wisher-extrahard-start/letter_templates/letter_2.txt") as file:
    file2 = [line.strip() for line in file.readlines()]

list_files.append(file2)
with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 32/birthday-wisher-extrahard-start/letter_templates/letter_3.txt") as file:
    file3 = [line.strip() for line in file.readlines()]

list_files.append(file3)    

if send_email:
    email_letter = random.choice(list_files)
    #replacing the [NAME] with the person's name


# 4. Send the letter generated in step 3 to that person's email address.




# #################################
# import datetime as dt
# import pandas as pd
# import random 
# import smtplib

# now = dt.datetime.now()
# month = now.month
# day =  now.day
# today_tuple = (month, day)

# data = pd.read_csv("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 32/birthday-wisher-extrahard-start/birthdays.csv")

# #dictionary comprehension
# data_dict ={(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}
# print(data_dict)


# if today_tuple in data_dict:
#     birthday_person = data_dict[today_tuple]
#     file_path =f"/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 32/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as file:
#         contents = file.read()
#         contents = contents.replace("[NAME]", birthday_person['name'])

#     #creating a email connection for the email
#     email = "hiddenhills@gmail.com "
#     password ="ola"

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=email, password=password)
#         connection.sendmail(
#             from_addr=email , 
#             to_addrs="helloworld@gmail.com", 
#             msg=f"Subject:Happy Birthday! \n\n {contents}"
#             )