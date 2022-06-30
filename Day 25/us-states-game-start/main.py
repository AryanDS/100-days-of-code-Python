import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image="/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)

is_game_on=True

#Calling the 50_States.csv file

states_data = pd.read_csv("/Users/aryansaini/Documents/Visual Studio Code/100 days of code/100-days-of-code-Python/Day 25/us-states-game-start/50_states.csv")
print(states_data)


#Checking if the user guess is correct or not!
states_list = states_data["state"].to_list()
guessed_state=[]

while len(guessed_state) < 50:
    #Getting user answer about the state
    answer_state= screen.textinput(title=f"{len(guessed_state)}/50 State Correct!", prompt="What's another states name?").title()
    
    

    if answer_state =="Exit":
        missing_states=[ state for state in states_list if state not in guessed_state]
        # missing_states=[]
        # for state in  states_list :
        #     if state not in guessed_state:
        #         missing_states.append(state)
        # print(missing_states)        
        new_states = pd.DataFrame(missing_states)
        new_states.to_csv("States_to_Learn.csv")        
        break
    if answer_state in states_list:
        guessed_state.append(answer_state)
    #Creating a new turtle
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        #getting the corrdinates of the states 
        state_data = states_data[states_data['state']== answer_state]
        t.goto(int(state_data.x) , int(state_data.y))
        t.write(state_data['state'].item()) #item() will fetch the first item from the data!
            
