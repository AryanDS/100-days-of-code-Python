#opening the weather_data.csv file

with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 25/weather_data.csv") as file:
    file_list = file.readlines()
    file_list= [i.strip("\n") for i in file_list]

print(file_list)    


#Using the readr () in the csv package
import csv

with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 25/weather_data.csv") as file:
    data = csv.reader(file)
    #data is a csv object which can be looped 
    temperature=[]
    for row in data:
       if row[1] != "temp":
        temperature.append(int(row[1]) )
    print(temperature)    
       

#Using pandas

import pandas as pd

df = pd.read_csv("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 25/weather_data.csv")
print(type(df))
print(type(df["temp"]))

#Converting DF data into dict

data_dict = df.to_dict()
print(data_dict)

#Converting a data series into a list

temp_list = df["temp"].to_list()
print(temp_list)

#Challenge
#Find the average temperature
avg_temp = sum(temp_list)/ len(temp_list)
print(avg_temp)

mean_temp = df["temp"].mean()
print(mean_temp)

#Challenge 
#Get the maximum temperature 
print(df["temp"].max())

#get the row 
print(df[df["day"] == "Monday"])

#Print the row of data where the temp was the maximum

print(df[df["temp"]== df["temp"].max()])


#Going deep into row 

monday = df[df.day == 'Monday']
print(type(monday))
print(monday.condition)
print(monday["condition"])

#Get monday's temperature and convert it into Fahranheit
temp =  monday["temp"]
#(celsius_1 * 1.8) + 32.
temp_fah = (temp*1.8)+32
print(temp_fah)



#Create a data frame from scratch 
data_dict={
    "Student":["Aryan","Anushka"],
    "Marks":[99,98]
}

data = pd.DataFrame(data_dict)
print(data)


#NYC Squirral data

df = pd.read_csv("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(df.columns)

gray_count = df[df["Primary Fur Color"]=="Gray"].shape[0]

black_count = df[df["Primary Fur Color"]=="Black"].shape[0]

red_count =df[df["Primary Fur Color"]=="Cinnamon"].shape[0]

print(gray_count)
print(black_count)
print(red_count)




#Creating a Dictionary 

data_dict={
    "Fur Color": ["Gray","Black","Red"],
    "Count": [gray_count,black_count, red_count]

}


#Create a data frame 

data= pd.DataFrame(data_dict)
print(data)

#To CSV

data.to_csv("Squirrel_data.csv")

