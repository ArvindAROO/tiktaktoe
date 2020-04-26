'''tik tak toe is a game between two players . Here is the code to enable the game for those who want to play and learn ''' 

choices = []

for i in range (0, 9) :
    choices.append(str(i+1))

playerOneTurn = True
winner = False

#creating the board
def printBoard() :
    print( '\n -------')
    print( ' |' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -------')
    print( ' |' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -------')
    print( ' |' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -------\n')

#the main part of the program 
while not winner :
    printBoard()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> "))
    except:
        print("please enter a valid field")
        continue
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        print("illegal move, plase try again")
        continue

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn
#checking for the possibility of winning 
    for i in range (0, 3) :
        j = i * 3
        if (choices[j] == choices[(j + 1)] and choices[j] == choices[(j + 2)]) :
            winner = True
            printBoard()
        if (choices[i] == choices[(i + 3)] and choices[i] == choices[(i + 6)]) :
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
