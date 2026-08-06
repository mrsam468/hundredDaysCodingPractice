import random
import art

print(art.logo)
still_wants_to_play = True
while still_wants_to_play:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


    def deal_card():
        return random.choice(cards)


    user_card = []
    computer_card = []
    total_computer_card = 0
    total_user_card = 0
    for card in range(1, 3):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    total_user_card = sum(user_card)
    total_computer_card = sum(computer_card)


    def win_lose():
        if total_computer_card == 21:
            return "computer wins"
        elif total_user_card == 21:
            return "you win"
        elif total_computer_card > 21:
            return "you win"
        elif total_user_card > 21:
            return "computer win"
        elif total_user_card > total_computer_card:
            return "you win"
        elif total_computer_card == total_user_card:
            return "draw"
        else:
            return "computer wins"


    no_winner_found = True
    while no_winner_found:
        if total_computer_card > 21:
            cards[0] = 1
        print(f"user card {user_card} = {total_user_card}")
        print(f"computer first card : {computer_card[1]}")
        if total_user_card > 21 or total_computer_card == 21:
            print(f"user card {user_card} = {total_user_card}")
            print(f"computer card {computer_card} = {total_computer_card}")
            print("computer wins")
            no_winner_found = False
        else:
            if total_computer_card < 16:
                computer_card.append(deal_card())
            still_wants_another_card = input("Do you want another card? (y/n) ").lower()
            if still_wants_another_card == "y":
                user_card.append(deal_card())
                total_user_card = sum(user_card)
                print(win_lose())
            else:
                print(win_lose())
                no_winner_found = False
    continue_or_not = input("Do you want to play again? (y/n) ").lower()
    if continue_or_not == "y":
        print("\n" * 20)
    else:
        still_wants_to_play = False
