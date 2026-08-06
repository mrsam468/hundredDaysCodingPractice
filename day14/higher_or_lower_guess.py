import random

import art
import game_data

print(art.logo)


def game():
    wants_to_continue_playing = True
    total_score = 0
    first_name = game_data.data[random.randint(0, len(game_data.data) - 1)]
    while wants_to_continue_playing:
        print(total_score)
        second_name = game_data.data[random.randint(0, len(game_data.data) - 1)]
        print(f"Compare A = {first_name["name"]},{first_name["description"]},{first_name["country"]}")
        print(art.vs)
        print(f"Against B = {second_name["name"]},{second_name["description"]},{second_name["country"]}")
        guess = input("Who has more followers? Type 'A' or 'B': ")
        if guess == 'B':
            if first_name["follower_count"] > second_name["follower_count"]:
                print(f"sorry that was wrong! total score : {total_score}")
                wants_to_continue_playing = False
            else:
                print(f"correct guess")
                total_score += 1
                first_name = second_name
        else:
            if first_name["follower_count"] < second_name["follower_count"]:
                print(f"sorry that was wrong! total score : {total_score}")
                wants_to_continue_playing = False
            else:
                print(f"correct guess")
                total_score += 1
                first_name = first_name


game()
