import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
total_player_win_cnt = 0
total_computer_win_cnt = 0
total_draw_cnt = 0
game_round_cnt = 0

while True:

    player_move = input("Choose [r]ock, [p]apper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Try again...")

    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}")

    if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        total_player_win_cnt += 1
        game_round_cnt += 1
        print("You win this round!")
        print(f"Your score is: {total_player_win_cnt}")
        print(f"Computer score is: {total_computer_win_cnt}")
    elif player_move == computer_move:
        total_draw_cnt += 1
        game_round_cnt += 1
        print("Draw!")
    else:
        total_computer_win_cnt += 1
        game_round_cnt += 1
        print("You lose this round!")
        print(f"Your score is: {total_player_win_cnt}")
        print(f"Computer score is: {total_computer_win_cnt}")

    if game_round_cnt == 5:
        break

if total_player_win_cnt >= 3:
    print("\033[0;32;40m You win!")
    print(f"Your score is {total_player_win_cnt}")
elif total_player_win_cnt == total_computer_win_cnt:
    print("\033[0;33;40m The game is Draw!")
else:
    print("\033[0;31;40m You lose the game!")
    print(f"Computer score is: {total_computer_win_cnt}")
