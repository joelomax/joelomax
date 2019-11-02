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


block = ["-", " ", " ", " ", " ", " ", " ", " ", " ", " "]
player_pieces = {
    'player1': '',
    'player2': ''
}

select_menu = 0
while select_menu == 0:
    select_player = input("player 1: what do you want to be, type X or O   ")
    if select_player == "0":
        print("please use O, not 0")
    elif select_player == "O":
        player_pieces['player1'] = "O"
        player_pieces['player2'] = "X"
        select_menu = 1
        break
    elif select_player == "X" or select_player == "x":
        player_pieces['player1'] = "X"
        player_pieces['player2'] = "O"
        select_menu = 1
        break
    else:
        print("please select a valid player marker")

display_board(block)

print("input 1 to 9 on the num pad to select which square to enter")

def getUserInput(playerNumber):
    validInput = False
    while validInput == False:
        try:
            player1_entry = int(input("player {}: where will you go?  ".format(playerNumber)))
            if int(player1_entry) in range(0, 10):
                validInput = True
            else:
                print("Please enter a valid number within 1 to 9!")
        except:
            print("Please enter a valid number! ex")

    return player1_entry

def isValidMove(player_entry):
    if block[int(player_entry)] != " ":
        print("space is not vacant!  ")
        return False
    else:
        return True

def endGame():
    if " " not in block:
        return True

turn_order = 0
while True:
    turn_order = 1 - turn_order #Nice!
    if endGame():
        break
    player_entry = getUserInput(turn_order)
    if (isValidMove(player_entry)):
        block[int(player_entry)] = player_pieces['player' + turn_order]
        print(len(block))
        display_board(block)

print("game over!")
