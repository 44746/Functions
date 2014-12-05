import random
number_counters = int(input("Please enter the number of counters: "))

while number_counters > 0:
    player1 =int(input("How many counters do you want to take off: "))
    if player1 <=3 and player1 >0:
        number_counters = number_counters - player1
        
        if number_counters> 0:
            computer1 = random.randint(1,3)
            print("The computer chose {0}".format(computer1))
            number_counters = number_counters - computer1
            
            if number_counters <1:
                print("Player one wins")
            
        else:
            print("The computer wins!")
    else:
             print("Invalid number entered, go again")
