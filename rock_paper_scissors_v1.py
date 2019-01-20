import random

data = ["Rock", "Paper", "Scissors", "Quit", "rock", "paper", "scissors", "quit"]
score = { "user": 0, "computer":0, "tie":0 }
comp_data = ["Rock", "Paper", "Scissors"]
win_list = (("paper", "rock"), ("rock", "scissors"),("scissors", "paper"))

def getuser():
    name = input("Enter your name:")
    while True:
        userchoice = input ("Hello " + name + "! Please enter rock, paper, scissors or quit:")
        if userchoice not in data:
            print ("Enter the right choice")
        else:
            break
    return userchoice

def getcomp():
    comp_choice = random.choice(comp_data)
    print ("The Computer picks", comp_choice)
    return comp_choice

def whowins(userchoice, compchoice):
    if (userchoice == compchoice):
        win = "tie"
    elif (userchoice,compchoice) in win_list:
        win = "user"
    else :
        win = "computer"
    return win

def main():
    while True:
        userchoice = getuser()
        if (userchoice == quit):
            break
        compchoice = getcomp()
        winner = whowins(userchoice, compchoice)
        if winner == "user":
            print ("User wins")
        elif winner == "computer":
            print ("Computer Wins")
        elif winner == "tie" :
            print ("Tie")
        else:
            print ("Internal Error occured. Try again later!")
            break
        score[winner]+= 1

        if (score["user"] == 1):
            print (name, "won")


if __name__ == "__main__":
    main()
