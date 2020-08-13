import random

play = True

options = ["Yes", "No", "Can't say for sure", "You should give it a try", "Try looking at it another way",
           "It probably is as you think it", "Maybe", "Go for it!"]

while play:
    try:
        runs = int(input("How many questions do you want to ask?: "))
        play = False
        for run in range(0, runs):
            question = input("Enter your question here: ")
            index = random.randint(0, 7)
            print(options[index])
    except ValueError:
        print("Enter a number to know the number of questions you want to ask")
