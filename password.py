import time

# -----------------------------
# GAME SETTINGS
# -----------------------------

levels = [
    {
        "name": "Easy",
        "password": "apple",
        "hints": [
            "🍎 Hint: It is a fruit.",
            "💡 Hint: It can be red or green.",
            "🔎 Hint: It starts with 'a'."
        ]
    },
    {
        "name": "Medium",
        "password": "python",
        "hints": [
            "🐍 Hint: It is related to programming.",
            "💡 Hint: It is also an animal.",
            "🔎 Hint: It starts with 'p' and has 6 letters."
        ]
    },
    {
        "name": "Hard",
        "password": "secret",
        "hints": [
            "🤫 Hint: You should keep it private.",
            "💡 Hint: It starts with 's' and ends with 't'.",
            "🔎 Hint: It has 6 letters."
        ]
    }
]


# -----------------------------
# WELCOME SCREEN
# -----------------------------

def show_welcome():
    print("=" * 45)
    print("       🔐 PASSWORD CHALLENGE")
    print("=" * 45)
    print("Can you defeat all 3 security levels?")
    print("You have 3 attempts for each level.")
    print("=" * 45)
    print()


# -----------------------------
# PLAY LEVEL
# -----------------------------

def play_level(level, score):
    password = level["password"]
    hints = level["hints"]

    attempts = 0
    max_attempts = 3

    print(f"\n🔓 LEVEL: {level['name'].upper()}")
    print("-" * 45)

    while attempts < max_attempts:

        guess = input("🔑 Enter password: ")

        if guess.lower() == password.lower():
            print("✅ ACCESS GRANTED!")

            # More points for fewer attempts
            points = (max_attempts - attempts) * 100
            score += points

            print(f"⭐ You earned {points} points!")
            print(f"🏆 Current score: {score}")

            return score, True

        attempts += 1

        print("❌ ACCESS DENIED!")

        # Progressive hints
        if attempts <= len(hints):
            print(hints[attempts - 1])

        # Remaining attempts
        remaining = max_attempts - attempts

        if remaining > 0:
            print(f"❤️ Attempts remaining: {remaining}")

    print("\n🔒 SECURITY SYSTEM LOCKED!")
    print(f"The password was: {password}")

    return score, False


# -----------------------------
# FINAL RESULT
# -----------------------------

def show_result(score):
    print("\n" + "=" * 45)
    print("             🏆 GAME COMPLETE")
    print("=" * 45)

    print(f"⭐ Final Score: {score}")

    if score >= 700:
        print("👑 Rank: PASSWORD MASTER")
    elif score >= 500:
        print("🥇 Rank: SECURITY EXPERT")
    elif score >= 300:
        print("🥈 Rank: PASSWORD HUNTER")
    else:
        print("🥉 Rank: BEGINNER HACKER")

    print("=" * 45)


# -----------------------------
# MAIN GAME
# -----------------------------

def main():

    while True:

        show_welcome()

        score = 0

        start_time = time.time()

        for level in levels:

            score, passed = play_level(level, score)

            if not passed:
                print("\n💀 GAME OVER!")
                break

        else:
            # This runs only if all levels are completed
            end_time = time.time()
            total_time = round(end_time - start_time, 2)

            print(f"\n⏱️ Completion time: {total_time} seconds")

            # Speed bonus
            if total_time < 30:
                score += 200
                print("⚡ SPEED BONUS: +200 points!")

            show_result(score)

        play_again = input("\n🔄 Play again? (yes/no): ")

        if play_again.lower() != "yes":
            print("\n👋 Thanks for playing!")
            break


# Start the game
main()