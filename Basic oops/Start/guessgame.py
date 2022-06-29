secretWord = "giraffe"
guess = ""
tries = 0
outOfGuess = False

while (guess != secretWord and tries < 3):
    guess = input("guess!! :")
    tries += 1
    if(tries == 3):
        outOfGuess = True

if (outOfGuess == False):
    print("you won")
else:
    print ("you lost")