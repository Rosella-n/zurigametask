import random



while True:
        print("Enter choice 1-rock, 2-paper, 3-scissor")
        picked=int(input('Pick one option : '))
       
        while picked > 3 or picked < 1:
            picked= int(input("Enter valid option: "))
        if picked== 1:
            picked_value="Rock"
        elif picked==2:
            picked_value="Paper"
        else:
            picked_value="Scissor"
        print ("Player choice is: ",picked_value)
        print ("Now it's computer turn!!")
        cpu_picked=random.randint(1, 3)
        while cpu_picked== picked:
            cpu_picked=random.randint(1, 3)
        if cpu_picked==1:
            cpu_value="Rock"
        elif cpu_picked==2:
            cpu_value="Paper"
        else:
            cpu_value="Scissor"
        print("Computer choice is: ",cpu_value)
        if ((picked==1 and cpu_picked==2)or (picked==2 and cpu_picked==1)):
            print("Paper win")
            result="Paper"
        elif((picked==1 and cpu_picked==3)or (picked==3 and cpu_picked==1)):
            print("Rock win")
            result="Rock"
        else:
            print("Scissor win")
            result="Scissor"
        if result==picked_value:
            print("Player wins")
        else:
             print("Computer wins")
        print("would you like to play again? Y/N")
        answer=input("").lower()
        if answer=="n":
            break
        print("Thank you for playing")
