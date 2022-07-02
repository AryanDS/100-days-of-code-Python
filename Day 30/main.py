# try:
#     file= open("hala.txt")
# except:
#     print("There is an error ")    


#For multiple error in try 

try:
    file = open("ola.txt")    
    dict_ = {'key':'value'}
    print(dict_['olo'])

except FileNotFoundError:
    file = open("dummy1.txt", "w")
    file.write("checking ")
    print("No dict error checked ")    

except KeyError as error_key:
    print("Key error ")

else:
    content =  file.read()
    print(content)


finally:
    file.close
    print("I will close the file and execute anyways ")

#Printing the error message to know what caused the error 

# try:
#     dict1 ={"olo":1}
#     print(dict1['12'])
# except KeyError as error_key:
#     print(f"{error_key} is the error ")    

#Raising your error

# try:
#     file = open("ola.txt")    
#     dict_ = {'key':'value'}
#     print(dict_['olo'])

# except FileNotFoundError:
#     file = open("dummy1.txt", "w")
#     file.write("checking ")
#     print("No dict error checked ")    

# except KeyError as error_key:
#     print("Key error ")

# else:
#     content =  file.read()
#     print(content)


# finally:
#     raise TypeError("This is the error i made up!")


#Calculating BMI

height =int(input("Enter your height"))
weight =  int(input("Enter your weight"))

if height >3:
    raise ValueError("Human height should not exceed 3 metres!")

bmi = weight / height **2

print(bmi)