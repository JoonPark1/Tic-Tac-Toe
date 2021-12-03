'''Here, we are defining the game board using a dictionary called game_board.
Each position of a three by three matrix game_board is indexed by a unique number.
The game_board will update itself after every player's turn.'''

game_board = {'7': ' ', '8': ' ', '9': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '1': ' ', '2': ' ', '3': ' '}
game_board_lst_keys = []
for number in game_board:
    game_board_lst_keys.append(number)
assert(game_board_lst_keys == ['7', '8', '9', '4', '5', '6', '1', '2', '3']), "The game_board is not oriented correctly!"
def print_game_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def start_game():
    player = 'A'
    turn = 0
    #At every turn of a player, the game board is printed.
    #As long as the player chooses the appropriate box number,
    #they are allowed to fill the box and make their move.
    for i in range(10):
        print_game_board(game_board)
        print("It's your turn, " + player + ". Where would you like to move?")
        num = str(input())
        #Particular box is not filled yet. Fill it with player's label.
        if game_board[num] == ' ':
            game_board[num] = player
            turn += 1
        #If box is filled, then proposed box number is not valid.
        #Should alert the player in this case.
        else:
            print("The box is already full. Where else would you like to move?")
            continue
        #After 5 moves, there is a chance of a winner. Must check all 8 conditions.
        #For each row or column, check for false wins when we have empty rows or columns.
        if turn >= 5:
            #Check for the top row
            if game_board['7'] == game_board['8'] == game_board['9'] != ' ':
                print_game_board(game_board)
                print("Game over!")
                print(player + " won!")
                break

            #Check for the middle row
            elif game_board['4'] == game_board['5'] == game_board['6'] != ' ':
                print_game_board(game_board)
                print("Game over!")
                print(player + " won!")
                break
            #Check for last row
            elif game_board['1'] == game_board['2'] == game_board['3'] != ' ':
                print_game_board(game_board)
                print("Game over!")
                print(player + " won!")
                break
            #Check for left column
            elif game_board['7'] == game_board['4'] == game_board['1'] != ' ':
                print_game_board(game_board)
                print("Game over!")
                print(player + " won!")
                break
            #Check for middle column
            elif game_board['8'] == game_board['5'] == game_board['2'] != ' ':
                print_game_board(game_board)
                print("Game over!")
                print(player + " won!")
                break
            #Check for right column
            elif game_board['9'] == game_board['6'] == game_board['3'] != ' ':
                print_game_board(game_board)
                print("Game over!")
                print(player + " won!")
                break
            #Check for downwards right diagonal
            elif game_board['7'] == game_board['5'] == game_board['3'] != ' ':
                print_game_board(game_board)
                print("Game over!")
                print(player + " won!")
                break
            #Lastly, check for downwards left diagonal
            elif game_board['9'] == game_board['5'] == game_board['1'] != ' ':
                print_game_board(game_board)
                print("Game over!")
                print(player + " won!")
                break
            #After 9 moves, if there's no winner, declare a tie ending.
            if turn == 9:
                print("There is a tie!")
                print("Game over!")
                break
        #After every turn, we have to switch to the other respective player.
        if player == 'A':
            player = 'B'
        else:
            player = 'A'
    #Ask if the player wants to restart the game due to game over, which is done whenever we exit the for loop.
    answer = input("Do you want to play again? Say yes or no.")
    #Regardless of whether answer is yes or no, we must always reset the game_board.
    #Even if user does not want to continue and suddenly wants to start a new game,
    #he or she must do so by calling the start_game function.
    for number in game_board_lst_keys:
        game_board[number] = ' '
    if answer == "Yes" or answer == "yes":
        start_game()
        


if __name__ == "__main__":
    start_game()
            
            
        
    
    
    
