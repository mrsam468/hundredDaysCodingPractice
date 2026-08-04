print("welcome to treasure island \n your mission is to find the treasure")
direction = input("left or right\n")
if direction == "right":
    print("you fell into a pit")
elif direction == "left":
    decision = input("right or left\n")
    if decision == "Swim":
        print("you have been attacked by trout game over")
    elif decision == "wait":
        door = input("what door do you want? red or blue or yellow\n")
        if door == "red":
            print("burned to fire game over")
        elif door == "yellow":
            print("you win")
        else:
            print("you lose")
    else:
        print("you lose")
else:
    print("you lose")