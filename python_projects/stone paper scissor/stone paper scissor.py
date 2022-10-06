import random

tie=0
user_wins=0
computer_wins=0
count=0
while count<5:
 computer = ["Stone", "Paper", "Scissor"]
 com_player = random.choice(computer)

 print("Enter 1 for Stone. 2 for paper. 3 for scissor")
 user = int(input("enter the user input-"))
 print("COMPUTER CHOOSES:",com_player)
 if user==1:
    count = count + 1
    if com_player=="Stone":
        print("TIE")
        tie=tie+1
    elif com_player=="Paper":
        print("COMPUTER WINS")
        computer_wins=computer_wins+1
    elif com_player=="Scissor":
        print("USER WINS")
        user_wins=user_wins+1

 elif user==2:
    count = count + 1
    if com_player=="Stone":
        print("USER WINS")
        user_wins = user_wins + 1
    elif com_player=="Paper":
        print("TIE")
        tie=tie+1
    elif com_player=="Scissor":
        print("COMPUTER WINS")
        computer_wins=computer_wins+1
 elif user==3:
    count = count + 1
    if com_player=="Stone":
        print("COMPUTER WINS")
        computer_wins=computer_wins+1
    elif com_player=="Paper":
        print("USER WINS")
        user_wins=user_wins+1
    elif com_player=="Scissor":
        print("TIE")
        tie=tie+1
print("USER WINS-",user_wins,"TIE's-",tie,"COMPUTER WINS-",computer_wins)