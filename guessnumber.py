correct_pas="secrete"
attempt=0
print("Welcome to the secrte password system!")
print("You have 3 attempts to unlock it")
while attempt<3:
    guess=input("Enter password: ")
    if guess==correct_pas:
        print("Access Granted")
        break
    else:
        attempt+=1
        print("Invalid password")
    if attempt==1:
        print("Hint:It is something u should keep private")
    elif attempt==2:
        print("Hint:It start with s and end with t")
    else:
        print("Level 3 failed")
if attempt==3:
    print("Game Over")
else:
    print("\nCONGRATULATIONS!")