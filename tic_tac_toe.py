def display_board(block):
    print("    |     |    ")
    print(block[7]+"   |  "+block[8]+"  |  "+block[9])
    print("    |     |    ")
    print("_______________")
    print("    |     |    ")
    print(block[4]+"   |  "+block[5]+"  |  "+block[6])
    print("    |     |    ")
    print("_______________")
    print("    |     |    ")
    print(block[1]+"   |   "+block[2]+" |   "+block[3])
    print("    |     |    ")

winstates = [
	[1,2,3],
	[4,5,6],
	[7,8,9],
	[1,4,7],
	[2,5,8],
	[3,6,9],
	[1,5,9],
	[3,5,7]
]

block = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player_pieces = {
    'player1': '',
    'player2': ''
}

while True:
    counter_selection = input(
        "player 1: what do you want to be, type X or O   ")
    if (counter_selection != 'X' or counter_selection != 'O'):
        print('Please type X or O')
        continue
    player_pieces['player1'] = counter_selection
    player_pieces['player2'] = "X" if counter_selection == "O" else "O"
    break

display_board(block)

print("input 1 to 9 on the num pad to select which square to enter")


def getUserInput(playerNumber):
    validInput = False
    while validInput == False:
        try:
            player1_entry = int(
                input("player {}: where will you go?  ".format(playerNumber)))
            if int(player1_entry) in range(1, 10):
                validInput = True
            else:
                print("Please enter a valid number within 1 to 9!")
        except:
            print("Please enter a valid number! ex")

    return player1_entry


def isValidMove(player_entry):
    if block[int(player_entry) -1] != " ":
        print("space is not vacant!  ")
        return False
    else:
        return True


def endGame():
    if " " not in block:
        return True

def decideWinner():
    for item in winstates:
		line = ''
		for i in item:
			line += block[i]
			if line[:] == 'O':

			win = 0
			return win
turn_order = 0
while True:
    turn_order = 1 - turn_order  # Nice!
    if endGame():
        break
    player_entry = getUserInput(turn_order)
    if (isValidMove(player_entry)):
        block[int(player_entry)] = player_pieces['player' + str(turn_order + 1)]
        print(len(block))
        display_board(block)


decideWinner()
print("game over!")
