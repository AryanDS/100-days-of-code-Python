from game_data import data
import random
import art


#############################

#display art

#generate random account from data

def format_account(account):
    """format account data into a printable format"""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, {account_country} "


def check_answer(guess, a_followers, b_followers):
    # if a_followers > b_followers:
    #     return guess == 'a'
    # else:
    #     return guess == 'b'
    return guess == 'a' if a_followers > b_followers else guess == 'b'


print(art.logo)
game_continue = True
account_a =random.choice(data)
account_b = random.choice(data)

while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}")
    print(art.vs)
    print(f"Against B: {format_account(account_b)}")


    #Ask user input 
    guess = input("Who has more followers? Type 'A' or 'B' ").lower()

    #get number of followers
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b["follower_count"]

    score=0

    #check if user is correct 
    is_correct= check_answer(guess, a_follower_count, b_follower_count)

    #give user feedback 
    if is_correct:
        score+=1
        print(f"You're right, Current Score: {score}")
        account_a = 

    else:
        print(f"You are wrong!, Final Score: {score}")

        game_continue = False

