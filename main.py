while True:
    choice = print('''Hello, welcome to this simple game of Rock-Paper-Scissors
    Enter: "R" to pick Rock
        "P" to pick paper
        "S" to pick scissors''')

    user_input = input("What is your choice? ")


    import random
    list = ["Rock", "Paper", "Scissors"]

    cpu_choice = random.choice(list)

#if user picks R(rock)
    if user_input.upper() == "R":
        print(f"Player(Rock) : CPU({cpu_choice})")
        if cpu_choice == "Rock":
            print("That's a tie. Try again.")
        elif cpu_choice == "Paper":
            print("You lose.Better luck next time!")
            break
        elif cpu_choice == "Scissors":
            print("You win!")
            break
        else:
            print("invalid")

#if user picks P(paper)
    elif user_input.upper() == "P":
        print(f"Player(Paper) : CPU({cpu_choice})")
        if cpu_choice == "Rock":
            print("You win!")
            break
        elif cpu_choice == "Paper":
            print("That's a tie. Try again.")
        elif cpu_choice == "Scissors":
            print("You lose.Better luck next time!")
            break
        else:
            print("invalid")

#if user picks S(scissors)
    elif user_input.upper() == "S":
        print(f"Player(Scissors) : CPU({cpu_choice})")
        if cpu_choice == "Scissors":
            print("That's a tie. Try again.")
        elif cpu_choice == "Rock":
            print("You lose.Better luck next time!")
            break
        elif cpu_choice == "Paper": 
            print("You win!")
            break
        else:
            print("invalid") 

#if user picks neither R(rock), P(paper), nor S(scissors)     
    else:
        print("Invalid input!Try again.")



