print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("Left or Right, my friend?\n ").lower()
#case_direction = direction.lower()

if direction == "left":
    part2 = input("Smart move, now.. Swim... or Wait?!:\n").lower()
    #case_part2 = part2.lower()
    if part2 == "wait":
        part3 = input("Smart move, now.. which door? Red, Blue, or Yellow?\n").lower()
        # case_part3 = part3.lower()
        question = input("Are you sure? Yes or No... ").lower()
        if question == "yes":
            if part3 == "blue":
                print("Eaten by the beast.. Game Over")
            elif part3 == "yellow":
                print("You are the King! The Treasure is now yours. Enjoy your Kingdom!")
            elif part3 == "red":
                print("You walked into the abyss. No Return. Game Over.")
            else:
                print("You fool! You can't win that way... Game over.")
        else:
            print("You're unprecise and indecisive. You didn't survive")
    else:
        print(" Wrong Move.. The Mako feasted tonight on your bones. Game Over")
else:
    print("You fell in quicksand. It was slow, but no one was there for aid. Game Over.")
