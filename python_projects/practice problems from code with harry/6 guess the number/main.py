"""You have to use the following three methods to reserve a list:

Inbuild method of python
List name [::-1] slicing trick
Swap the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]
"""
import random

def guess(b):
    a=b
    user_input = int(input("Enter the guessed number"))
    count = 1
    while user_input != a:
        count=count+1
        if user_input > a:
            print(f"your Input {user_input} is larger than Correct Number. Please Enter value less than {user_input}")
            user_input = int(input("Enter the guessed number"))
        elif user_input < a:
            print(f"Your Input {user_input} is smaller than Correct Number. Please Enter value greater than {user_input}")
            user_input = int(input("Enter the guessed number"))

    print(f"You guess the correct number {user_input} in {count} trial")
    return count
if __name__ == '__main__':

    print("Guess the correct number between 0 and 20")
    a=random.randint(0,20)
    print("Player 1 chance")
    trial_1=guess(a)
    b = random.randint(0, 20)
    print("Player 2 chance")
    trial_2=guess(b)
    if trial_1>trial_2:
        print("player 2 wins")
    elif trial_1<trial_2:
        print("player 1 wins")
    else:
        print("game draw")

    print(f"the correct numbers for player 1 and player 2 are {a} and {b}")



