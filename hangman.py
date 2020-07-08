def hangman(word):
    wrong = 0
    stages = ["",
              "_________      ",
              "|        |     ",
              "|        |     ",
              "|        0     ",
              "|       /|\    ",
              "|       / \    ",
              "|              "]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter "
        char = input(msg)
        if char in remaining_letters:
            cind = remaining_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))


import random
wordlist = ["hola","abyss","jazzy","ivory","jawbreaker",
            "lucky","kiosk","knapsack","oxygen","microwave"]
n = random.randint(0,len(wordlist)-1)
#print(n)
hangman(wordlist[n])