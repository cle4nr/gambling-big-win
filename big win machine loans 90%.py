import random
bal = 10
bal = int(bal)
print("your balance is",bal)
yn = input("do you want to spin?\n")
yn = "y"
while yn == "y":
    slot1 = random.randint(1,9)
    slot2 = random.randint(1,9)
    slot3 = random.randint(1,9)
    if slot1 == slot2 == slot3:
        print(slot1,slot2,slot3, "\nJACKPOT WIN WOOOOOOOOOOOOOO") 
        bal += 100
        print("your balance is",bal)
        yn = input("do you want to spin again?\n")
        yn = "y"
    elif slot1 == slot2:
        print(slot1,slot2,slot3, "\nmini win")
        bal += 10
        yn = input("do you want to spin again?\n")
        yn = "y"
    elif slot2 == slot3:
        print(slot1,slot2,slot3, "\nmini win")
        bal += 10
        yn = input("do you want to spin again?\n")
        yn = "y"
    elif slot1 != slot2 != slot3:
        print(slot1,slot2,slot3, "\nlose")
        bal -=5
        print("your balance is",bal)
        yn = input("do you want to spin again?\n")
        yn = "y"
        print(bal)
    if bal <= 0:
        yn = ""
        print("you're out of money you need to take out a loan\n")
        shrkbank = input("do you want to use a Bank or a Loan Shark \n")       #change this to a click choice
        shrkbank = shrkbank.lower()
        if "bank" in shrkbank:
            bank = input("How much would you like to take out (cap is 2500) there is a 2% interest every day \n")
            bank = int(bank)
            if bank >= 2500:
                print("you cannot take out more than 2500")
                bank = input("How much would you like to take out (cap is 2500) there is a 2% interest every day \n")
            bank = int(bank)
            bal += bank
            yn = "y"
        elif "shark" in shrkbank:    
            print("from a loan shark you can get a loan from between 0 mush coins and 5000 mush coins")
            loansize = int(input("what size loan do you want to take out\n"))
            bal += loansize
            print("your balance is now",bal,"you must pay this back in 7 days or else there will be consequences")
            yn = input("do you want to spin again?\n")
            yn = "y"
        
        
            
            
            

        
        
        
        
        
        
    