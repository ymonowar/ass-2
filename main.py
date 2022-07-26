from random import randint
num_of_rolls = int(input("How many times roll the dice:"))
all_dice_rolls = []
for dice_rolls in range(num_of_rolls):
    dice =randint(1,6)
    all_dice_rolls.append(dice)
    print("List- rolls", dice)
print("Total for all of the rolls is:", sum(all_dice_rolls))
print("Avarage for all of the rolls is:", sum(all_dice_rolls)/len(all_dice_rolls))