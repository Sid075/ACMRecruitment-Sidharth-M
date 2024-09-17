import os
import random

spots = {1 : '1', 2 : '2', 3: '3', 4 : '4', 5 : '5', 
         6 : '6', 7 : '7',  8 : '8', 9 : '9'}

def draw_board(board):
    """Function to draw the Tic-Tac-Toe board."""
    print("\n")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("---+---+---")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("---+---+---")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("\n")

def check_for_win(board, player):
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[1, 4, 7], [2, 5, 8], [3, 6, 9],[1, 5, 9], [3, 5, 7]  ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False   

def is_draw(board):
    return all(board[key] in ['X', 'O'] for key in board)

def player_turn():
    while True:
        choice = input("Player's turn: Pick your spot (1-9) or press 'q' to quit: ")
        if choice.lower() == 'q':
            return 'q'
        if choice.isdigit() and int(choice) in spots and spots[int(choice)] not in ['X', 'O']:
            return int(choice)
        else:
            print("Invalid move, try again.")

def computer_turn():
    while True:
        computer_move = random.randint(1, 9)
        if spots[computer_move] not in ['X', 'O']:
            print(f"Computer chose: {computer_move}")
            return computer_move
        
def main():
    playing = True
    current_player = 'X'  
    
    while playing:
        os.system('cls' if os.name == 'nt' else 'clear')
        draw_board(spots)

        if current_player == 'X': 
            choice = player_turn()
            if choice == 'q':
                playing = False
                break

            spots[choice] = 'X'
            if check_for_win(spots, 'X'):
                os.system('cls' if os.name == 'nt' else 'clear')
                draw_board(spots)
                print("Player wins!")
                break
            if is_draw(spots):
                os.system('cls' if os.name == 'nt' else 'clear')
                draw_board(spots)
                print("It's a draw!")
                break
            current_player = 'O'  
        else: 
            choice = computer_turn()
            spots[choice] = 'O'  

            if check_for_win(spots, 'O'):
                os.system('cls' if os.name == 'nt' else 'clear')
                draw_board(spots)
                print("Computer wins!")
                break

            if is_draw(spots):
                os.system('cls' if os.name == 'nt' else 'clear')
                draw_board(spots)
                print("It's a draw!")
                break

            current_player = 'X'  


main()
