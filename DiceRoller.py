import random
start = 'Y'
while start == 'Y':
    start = input("Do you want to roll the dice [Y/N]: ")
    if start == 'Y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(dice1,dice2)
    else:
            print("done")
    
      
    
        
