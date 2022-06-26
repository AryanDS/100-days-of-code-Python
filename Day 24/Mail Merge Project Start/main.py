#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

"""
Main code below
"""

#calling the main file and printing the same 
# with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 24/Mail Merge Project Start/Output/ReadyToSend/example.txt") as file:
#     file_contents= file.read()
#    # print(file_contents) 


#calling the starting the letter.
with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
    starting_file= file.read()
    # print(starting_file)


with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 24/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
    names = [i.strip('\n') for i in names]
    # print(names)


print(starting_file)   
print(names) 

for name in names:
    #replacing the name
    ready_to_send = starting_file.replace("[name]", name)
    print(ready_to_send)
    
    with open("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 24/Mail Merge Project Start/Output/ReadyToSend/"+str(name)+".txt", mode="w" ) as file:
        file.write(ready_to_send)



