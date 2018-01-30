from random import randint

dice_1 = 0
dice_11 = 0
dice_2 = 0
total_1 = 12
total_2 = 26


exits = 1

while exits != 0:
    print ("\t\tDice Simulator")
    print ("RULES:\ni. If you can roll the single dice up to 3 times and not pass total of 12, you will win this game.") 
    print ("ii. And for double dice if you roll up to 3 times and not pass 26, you will win.\n")
    print ("\t1. Single Dice\n\t2. Double Dice\n\t9. Exit")
    userchoice=input("\nYour choose: ")
    if int(userchoice) == 1:
        roll_1 = randint(1,6)
        roll_2 = randint(4,6)
        roll_3 = randint(1,6)
        dice_1 = roll_1 + roll_2 + roll_3
        input("Press enter to roll the dice....\n\n")
        print ("\tYour first dice is:",roll_1)
        input("\nPress enter again to roll the next dice....\n\n")
        print ("\tYour second dice is:",roll_2)
        input("\nPress enter to roll the last dice....\n\n")
        print ("\tYour third dice is:",roll_3)
        input("\nPress enter see the results....\n\n")
        if dice_1 <= total_1:
            print ("\nTotal for 3 times roll =",dice_1)
            print ("\n\t\tCongratulation you win this game!\n\n")
            b = input("Press enter to next game, 0 + enter for quit: ")
            if int(b) == 0:
                break
        else:
            print ("\nTotal for 3 times roll =",dice_1)
            print ("Sorry you are not lucky, you can try next game!")
        input()
    elif int(userchoice) == 2:
        roll_1 = randint(1,6)
        roll_2 = randint(3,6)
        roll_3 = randint(1,6)
        roll_4 = randint(1,6)
        roll_5 = randint(4,6)
        roll_6 = randint(1,6)
        dice_11 = roll_1 + roll_3 + roll_5
        dice_2 = roll_2 + roll_4 + roll_6
        input("Press enter to roll the dice....\n\n")
        print ("\tYour first dice is:",roll_1,"and",roll_2 )
        input("\nPress enter again to roll the next dice....\n\n")
        print ("\tYour second dice is:",roll_3,"and",roll_4 )
        input("\nPress enter to roll the last dice....\n\n")
        print ("\tYour third dice is:",roll_5,"and",roll_6 )
        input("\nPress enter see the results....\n\n")
        dices = dice_11 + dice_2
        if dices <= total_2:
            print ("\nTotal for 3 times roll =",dices)
            print ("\n\t\tCongratulation you win this game!\n\n")
            b = input("Press enter to next game, 0 + enter for quit: ")
            if int(b) == 0:
                break
        else:
            print ("\nTotal for 3 times roll =",dices)
            print ("Sorry you are not lucky, you can try next game!")
    elif int(userchoice) == 9:
        print ("\t\tGoodBye~~")
        input()
        exits -= 1
        
    else:
        print ("\nPlease enter the number given")
        input()
