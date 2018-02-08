import random

rock_count = 0.0
scissor_count = 0.0
paper_count = 0.0
total = 0

rock_chance = 0.0
scissor_chance = 0.0
paper_chance = 0.0

def probability(count,total):
    if total == 0:
        total = 1
    return float(count/total)

def nextplaybycomputer(input):
    global rock_count
    global scissor_count
    global paper_count
    global total
    global rock_chance
    global scissor_chance
    global paper_chance
    if input == 'rock':
        rock_count += 1
        total += 1
    elif input == 'scissor':
        scissor_count += 1
        total += 1
    elif input == 'paper':
        paper_count += 1
        total += 1
    rock_chance = probability(rock_count,total)
    scissor_chance = probability(scissor_count,total)
    paper_chance = probability(paper_count,total)
    print("rock chance : "+str(rock_chance)+" paper chance : "+str(paper_chance)+" scissor chance : "+str(scissor_chance))
    print("rock count : "+str(rock_count)+" paper count : "+str(paper_count)+" scissor count : "+str(scissor_count))
    if max(rock_chance,scissor_chance,paper_chance) == rock_chance:
        return 'paper'
    elif max(rock_chance,scissor_chance,paper_chance) == scissor_chance:
        return 'rock'
    elif max(rock_chance,scissor_chance,paper_chance) == paper_chance:
        return 'scissor'

def play(usermove,computermove):
    if usermove == computermove:
        print("Tie!")
    elif usermove == "rock" and computermove == "paper":
        print("You Lose!")
    elif usermove == "rock" and computermove == "scissor":
        print("You Win!")
    elif usermove == "paper" and computermove == "scissor":
        print("You Lose!")
    elif usermove == "paper" and computermove == "rock":
        print("You Win!")
    elif usermove == "scissor" and computermove == "rock":
        print("You Lose!")
    elif usermove == "scissor" and computermove == "paper":
        print("You Win!")

if __name__ == "__main__":
    game_set = ['rock', 'paper', 'scissor']
    firsttime = True
    count = 0
    nextmove = random.choice(game_set)
    n = int(input("Enter the number of time you want to play : "))
    while(count <= n):
        usermove = input("Please choose from [rock, paper, scissor] : 20")
        if(firsttime == True):
            firsttime = False
            computermove = random.choice(game_set)
            play(usermove,computermove)
        else:
            play(usermove,nextmove)
        nextmove = nextplaybycomputer(usermove)
        count = count+1



