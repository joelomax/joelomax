def display_board(block):
    print("    |     |   ")
    print(block[7]+"|"+block[8]+"|"+block[9])
    print("    |     |    ")
    print("_______________")
    print("    |     |    ")
    print(block[4]+"|"+block[5]+"|"+block[6])
    print("    |     |    ")
    print("_______________")
    print("    |     |    ")
    print(block[1]+"|"+block[2]+"|"+block[3])
    print("    |     |    ")
 
block = ["-"," "," "," "," "," "," "," "," "," "]

select_menu = 0
select_player = input("player 1: what do you want to be, type X or O")
while select_menu == 0:
    if select_player == "0":
        print("please use O, not 0")
    elif select_player == "O" or select_player == 0:
        player1_piece = "O"
        player2_piece = "X"
    elif select_player == "X" or select_player == "x":
        player1_piece = "X"
        player2_piece = "O"
    else: 
        print("please select a valid player marker")
    select_menu = 1

display_board(block)

print("input 1 to 9 on the num pad to select which square to enter")

game_over = 0
turn_order=1
while game_over == 0:
    if turn_order == 1:
        player1_entry = int(input("player 1: where will you go?  "))
        entry_slice = slice(player1_entry)
        if block[entry_slice] != " ":
            print("space is not vacant!  ")
        elif block[entry_slice] == player1_piece:
            print("player 2's piece should be different than yours!  ")
        else:
            block.insert(player1_entry, player1_piece)
            block.remove(player1_entry+1)
            turn_order=0
            display_board(block)
    elif turn_order == 0:
        player2_entry = int(input("player 2: where will you go?  "))
        entry_slice = slice(player2_entry)
        if block[entry_slice] != " ":
            print("space is not vacant!")
        elif block[entry_slice] == player1_piece:
            print("player 1's piece should be different than yours!")
        else:
            block.insert(player2_entry, player2_piece)
            block.remove(player2_entry+1)
            turn_order=1
            display_board(block)
    elif all(block) != " ":
        game_over == 1
        
print("game over!")
