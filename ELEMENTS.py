# Import random module foe elements, random for computer
from random import randint

#user_name = int(input("what is your name?"))

#-----------------input------------#

repeat = True

while repeat:
    # TODO: display ask how many rounds you want to play
        # print("how many rounds do you want to play?")
        pass 

    # TODO: take the input from user choice for rounds
    # rounds=int(input("Enter your choice from above :"))
        pass

    # TODO : ask user for their name
        print("hello who is playing?")
        user = (input("enter name:"))

    # TODO: pick your choice on your element fire, water, grass
        print("Enter your choose of a battle element: 1 - fire  2 - water  3 - nature 4 - earth 5 - Poison")
        
    # TODO: take the input from user choice for thier choice
        user_choice=int(input("Enter your battle element?"))

    # TODO: choose either for your chocies 1=fire, 2=water, 3=grass, 4=nature, 5=lightning
        if user_choice == 1:
            choice_name= "fire"
        elif user_choice == 2:
         choice_name= "water"
        elif user_choice == 3:
           choice_name= "nature"
        elif user_choice == 4:
           choice_name= "earth"
        else:
            choice_name= "Poison"

    # TODO: the computer enters it choice 1=fire, 2=water, 3=grass, also make it random with randiant,
        computer_choice = randint(1,5)
        
    # TODO: computer choice vs user choice 
        while computer_choice == user_choice:
          computer_choice = randint(1,5)
            
        # computer choices is just like Players just copy and change
        if computer_choice == 1:
          computer_choice_element = "fire"
        elif computer_choice == 2:
           computer_choice_element = "water"
        elif computer_choice == 3:
          computer_choice_element = "nature"
        elif computer_choice == 4:
           computer_choice_element = "earth"
        else:
            computer_choice_element = "Poison"

    # TODO: show Player and computers choice
        print(choice_name,"Vs",computer_choice_element)

    # show problem for a tie for both guesses
        if user_choice == computer_choice:
            print("its a tie. let's try again!")

    # how to win with water
        if (user_choice==2 and computer_choice==5):
         print("poison wins, computer will rule")
        elif (user_choice==2 and computer_choice==4):
         print("water wins, humans will unplug computer")
        elif (user_choice==2 and computer_choice==3):
           print("nature wins, computer can see though human")
        elif (user_choice==2 and computer_choice==1):
         print ("water wins, human will overcome")
         
    # TODO: how to win with fire   
        if (user_choice==1 and computer_choice==5):
            print("fire wins, humans built computers")
        elif (user_choice==1 and computer_choice==4):
            print("earth wins, computers get better every month")
        elif (user_choice==1 and computer_choice==3):
           print("fire wins, humans know more")
        elif (user_choice==1 and computer_choice==2):
           print("water wins computer will out smart human")

    # TODO: how to win with nature     
        if (user_choice==3 and computer_choice==5):
            print("poison wins, computers are getting better")
        elif (user_choice==3 and computer_choice==4):
            print("nature wins, humans understand everything")
        elif (user_choice==3 and computer_choice==2):
            print("nature wins, humans win again")
        elif (user_choice==3 and computer_choice==1):
           print("fire wins, stupid humans dont understand")

    # TODO: how to win with earth     
        if (user_choice==4 and computer_choice==5):
            print("earth wins, humans smash computers")
        elif (user_choice==4 and computer_choice==3):
            print("nature wins, computer is on a roll")
        elif (user_choice==4 and computer_choice==2):
            print("water wins, computer will rule")
        elif (user_choice==4 and computer_choice==1):
            print("earth wins, humans are on another level")
            
    # TODO: how to win with poison   
        if (user_choice==5 and computer_choice==4):
            print("Earth wins, computer rule")
        elif (user_choice==5 and computer_choice==3):
            print("poison wins, humans made computers")
        elif (user_choice==5 and computer_choice==2):
            print("poison wins, humans are smarter")
        elif (user_choice==5 and computer_choice==1):
            print("fire wins, computers are getting smarter")

        print(f"your choice is {user_choice} and computers choice is {computer_choice}")

    # TODO: display results after the rounds are done
        print(f"Thanks for playing!: {user}")
        print("Do you want to play again? yes or no?:")
        repeat = ("y" or "yes") in input().lower()