import random  # para makagamit tayo ng random number

# 1. Gumawa ng secret number (1 hanggang 100)
secret_number = random.randint(1, 100)

print("🎮 Welcome to Guess the Number Game!")
print("Hulaan mo ang number (1 to 100).")

# 2. Gumawa ng loop para makapag-try si user ng paulit-ulit
while True:
    # Kumuha ng input kay user
    guess = input("Ilagay hula mo: ")

    # Check kung number ba yung in-enter
    if not guess.isdigit():
        print("❌ Paki-type number lang, hindi text.")
        continue  # balik sa loop

    guess = int(guess)  # convert input to integer

    # 3. Check kung tama hula
    if guess == secret_number:
        print("🎉 Tama! Ang secret number ay:", secret_number)
        break  # tapusin na yung game
    elif guess < secret_number:
        print("📉 Masyadong mababa. Subukan mo ulit.")
    else:
        print("📈 Masyadong mataas. Try again.")
