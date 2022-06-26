#We opened the .txt file and stored it in the file variable!
file =  open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 24/my_file.txt")
#We read the file using the read() keyword and stored it in content
content = file.read()
#Printing the contents of the file
print(content)
#After the file has been opened we need to close the file and we do that by 
file.close()

"""
If we don't need to remember .close() , we can use the approach below
"""

with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 24/my_file.txt") as file:
    contents = file.read()
    print("Using the with keywork")
    print(contents)

#When we want to write something to the file , below will overwrite everything on the file (deleting the pervious contents! mode="w")

with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 24/my_file.txt", mode="w") as file1:
    file1.write("Ola")

#when you want to append the contents on the file and NOT delete the pervious contents of the file

with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 24/my_file.txt", mode = "a")   as file2:
    file2.write("\n Appending new contents to the file!")


#When we try to write to a file that does not exists we can use the below code to create a new file 
with open("new_file.txt", mode="w") as file:
    file.write("Hello this is a new file!")    

    