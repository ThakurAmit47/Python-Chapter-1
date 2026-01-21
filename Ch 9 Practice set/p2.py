import random

def game():
    print("you are playing the game..")
    score = random.randint(1, 99)
    #fetch the hiscore
    with open("p2_hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score is {score}")
    if(score>hiscore):
        #write the hiscore to the file
        with open("p2_hiscore.txt", "w") as f:
            f.write(str(score))

    return score
game()
