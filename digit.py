import random
print("="*45)
print(    "CYBER VAULT")
print("  SECURITY SYSTEM V1.0")
print("="*45)
print("\n UNAUTHORIZED ACCESS DETECTED!")
print("Your mission: Break through 3 security layers.")
print("You have 3 lives.\n")
lives=3
score=0

#Level 1

print("\n"+ "=" *45)
print( "Level 1 -Digit PIN Lock")
print("="*45)
pin=random.randint(100,999)
print("The vault requires a 3-digit PIN.")
print("Hint: Try to discover the correct PIN.")
attempt=0
print(f"💡 Hint: The PIN starts with {str(pin)[0]}")
while attempt<3:
    guess=input("Enter 3-digit Pin:")
    if not guess.isdigit():
        print("Please enter number only")
        continue
    if len(guess)!=3:
        print("PIN must contain extact 3 digit.")
        continue
    guess=int(guess)
    if guess==pin:
        print("Level 1 Unlocked!")
        score+=100
        break
    attempt+=1
    lives-=1
    print("ACCESS DENIED!")
    if guess<pin:
        print("Hint: PIN is Higher")
    else:
        print("Hint: PIN is Lower")
    print(f"Lives remaining: {lives} ")

if attempt==3:
    print("\n SECURITY LOCKDOWN!")
    print(f"The correct PIN was {pin}.")
    print("Level 1 failed!")
    print("Moving to Level 2...")
    

#Level2
print("\n"+ "="*45)
print("Level 2 - PASSWORD LOCK")
print("=" *45)
password="galaxy"
attempt=0
print("The system requires a secret password.")
print("You have 3 attempts.")
while attempt<3:
    guess=input("Enter password:")
    if guess.lower()==password.lower():
        print("Level 2 Unlocked!")
        score+=200
        break
    attempt+=1
    lives-=1
    print(" ACCESS DENIED!")

    if attempt == 1:
        print("Hint: You can see it in the night sky.")

    elif attempt == 2:
        print("Hint: The password starts with 'g'.")

    elif attempt == 3:
        print("Hint: It has 6 letters.")

    print(f"Lives remaining: {lives}")


if attempt == 3:
    print("\n SECURITY LOCKDOWN!")
    print("GAME OVER.")
    print("Level 2 failed!")
    print("Moving to Level 3...")

#level3
print("=" *45)
print("Level 3 -MASTER LOCK")
print("=" *45)
print("The final security system uses a logic puzzle.")
print()
print("2 → 6")
print("3 → 12")
print("4 → 20")
print("5 → ?")
print("\n Find the pattern!")

answer = input("Enter your answer: ")

if answer.isdigit():
    answer = int(answer)

    if answer == 30:
        print("MASTER LOCK UNLOCKED!")
        score += 300
        print("\n CYBER VAULT UNLOCKED!")
        print(f" Final Score: {score}")
    else:
        print("\n INCORRECT!")
        print(" MASTER LOCK FAILED!")
        print("GAME OVER.")

else:
    print("\n Invalid input!")
    print(" MASTER LOCK FAILED!")
    print("GAME OVER.")