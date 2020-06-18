print("Welcome to the Snake Water Gun Game Wizard!")
print("You will get 10 chances to win maximum times, after that the game will be over.")
def game():
    import random
    lst=["Snake","Water","Gun"]
    i=0
    z=0
    while(i<11):
        if i>9:
            print("Game Over, Baby!!")
            break
        n=input("Enter your choice (Snake, Water and Gun):").capitalize()
        c=random.choice(lst)
        print(c,":",i+1,"turn")

        if c==n:
            print("Try again!!\n")
            i=i+1
            continue
        elif c=="Snake":
            if n=="Water":
                print("You Lose and BOT won this time\n")
                i = i + 1
                continue
            elif n=="Gun":
                print("Congrats,You Win",z+1, "times and BOT lose\n")
                i = i + 1
                z=z+1
                continue
            else:
                print("Invalid Input!")
        elif c=="Water":
            if n=="Snake":
                print("Congrats,You Win",z+1, "times and BOT lose\n")
                i = i + 1
                z = z + 1
                continue
            elif n=="Gun":
                print("You Lose and BOT won, Better Luck next time\n")
                i = i + 1
                continue
            else:
                print("Invalid Input!")
        elif c=="Gun":
            if n=="Snake":
                print("You Lose and BOT won, Better Luck next time\n")
                i = i + 1
                continue
            elif n=="Water":
                print("Congrats,You Win",z+1, "times and BOT lose\n")
                i = i + 1
                z = z + 1
                continue
            else:
                print("Invalid Input!")
def repeat():
    call_repeat = input("Do you want to Play again?, Please type y for YES or n for NO.")
    if call_repeat == "y":
            game()
    elif call_repeat =="n":
            print("See You Later!!")
    else:
        repeat()

game()
repeat()