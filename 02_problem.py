import random

def game():
    print("you are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("hiscore.text") as f:
        hiscore = f.read()
        if(hiscore!=""):
             hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score: {score}")
    if(score>hiscore or hiscore==""):
        #write this hiscore to the file
        with open("hiscore.text", "w") as f:
            f.write(str(hiscore))

    return score

game


