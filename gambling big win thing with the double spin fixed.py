import random
bal = 1000
bal = int(bal)
print("your balance is",bal)
yn = input("do you want to spin?\n")
while yn == 'y':
    slot1 = random.randint(1,10)
    slot2 = random.randint(1,10)
    slot3 = random.randint(1,10)
    if slot1 == slot2 == slot3:
        print(slot1,slot2,slot3, "\nJACKPOT WIN WOOOOOOOOOOOOOO") 
        bal += 2000
        print("your balance is",bal)
        yn = input("do you want to spin again?\n")
    elif slot1 == slot2 != slot3:
        print(slot1,slot2,slot3, "\nmini win")
        bal += 10
        print("your balance is",bal)
        yn = input("do you want to spin again?\n")
    elif slot1 != slot2 == slot3:
        print(slot1,slot2,slot3, "\nmini win")
        bal += 10
        print("your balance is",bal)
        yn = input("do you want to spin again?\n")
    else:
        print(slot1,slot2,slot3, "\nlose")
        bal -=5
        print("your balance is",bal)
        yn = input("do you want to spin again?\n")

        
        
    