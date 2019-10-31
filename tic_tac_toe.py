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
 
block = ["-"," "," "," "," "," "," "," "," "," "]

select_menu = 0
while select_menu == 0:
    select_player = input("player 1: what do you want to be, type X or O   ")
    if select_player == "0":
        print("please use O, not 0")
    elif select_player == "O":
        player1_piece = "O"
        player2_piece = "X"
        select_menu = 1
        break
    elif select_player == "X" or select_player == "x":
        player1_piece = "X"
        player2_piece = "O" 
        select_menu = 1
        break
    else:
        print("please select a valid player marker")

display_board(block)

print("input 1 to 9 on the num pad to select which square to enter")

game_over = 0
turn_order=1
while game_over == 0:
    if " " not in block:
        game_over == 1
        break
    if turn_order == 1:
        try:
            player1_entry = int(input("player 1: where will you go?  "))
        except:
            tf=False
            while tf==False:
                player1_entry=input("Please enter a valid number!")
                try:
                    if int(player1_entry) in range(0,10):
                        tf=True
                except:
                    continue

        if block[int(player1_entry)] != " ":
            print("space is not vacant!  ")
        elif block[int(player1_entry)] == player2_piece:
            print("player 2's piece should be different than yours!  ")

        else:
            block[int(player1_entry)] = player1_piece
            print(len(block))
            turn_order=0
            display_board(block)
    elif turn_order == 0:

        try:
            player2_entry = int(input("player 2: where will you go?  "))
        except:
            tf=False
            while tf==False:
                player2_entry=input("Please enter a valid number!")
                try:
                    if int(player2_entry) in range(0,10):
                        tf=True
                except:
                    continue

        if block[int(player2_entry)] != " ":
            print("space is not vacant!  ")
        elif block[int(player2_entry)] == player1_piece:
            print("player 2's piece should be different than yours!  ")

        else:
            block[int(player2_entry)] = player2_piece
            print(len(block))
            turn_order=0
            display_board(block)

print("game over!")