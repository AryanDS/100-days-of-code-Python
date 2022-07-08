# import smtplib

"""
Using the SMTPLIB module to send emails
"""

# #My email credentials 
# email = "hiddenhills@gmail.com "
# password ="ola"
# #Creating an smtplib object which would connect to the email provider
# connection = smtplib.SMTP("smtp.gmail.com")

# #starttls calls the transport layer security protocol which would encrpyt the email sent, secure it basically 
# connection.starttls()

# connection.login(user=email, password=password)
# connection.sendmail(from_addr=email , to_addrs="helloworld@gmail.com", msg="Subject:Hello\n\n This is the body of my email")

# connection.close()

# #Above using the "with" keyword

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email , 
#         to_addrs="helloworld@gmail.com", 
#         msg="Subject:Hello\n\n This is the body of my email"
#         )


"""
Using the datetime module
"""
# import datetime as dt

# now = dt.datetime.now()
# print(dir(now))

# #tapping into the now object's attributes
# year=  now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()

# print(day_of_week)
# print(year)
# print(month)
# print(day)

# #Creating our own datetimme object

# date_of_birth = dt.datetime(year=1996, month=4, day=2)
# print(date_of_birth)



"""
Challenge of the day
"""
import random 
import datetime as dt
import smtplib

with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 32/Birthday Wisher (Day 32) start/quotes.txt") as file:
    data=[line.strip() for line in file.readlines()]
    
random_data = random.choice(data)

#Using datetime module to get the current weekday 
now = dt.datetime.now()

day_of_week = now.weekday()
print(day_of_week)

#Now we will check for current day and sent an email
email = "hiddenhills@gmail.com "
password ="ola"

if day_of_week == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email , 
            to_addrs="helloworld@gmail.com", 
            msg=f"Subject:Hello\n\n {random_data}"
            )
