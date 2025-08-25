# ============================
# GUESS THE NUMBER GAME 🎲
# ============================

# 1. Import the random library
# Bakit? Kasi hindi tayo pwedeng gumawa ng "totoong random" number
# gamit lang ng math. May built-in library si Python na gagawa nito.
import random

# 2. Gumawa tayo ng random number
# random.randint(1, 100) → ibig sabihin bubunot siya ng number
# mula 1 hanggang 100 (kasama ang 1 at 100).
secret_number = random.randint(1, 100)

# 3. Infinite loop gamit ang while True
# Ang loop na ito ay tuloy-tuloy hangga’t hindi natin sinasabing "break".
# Para siyang laro na walang tigil hanggang mahulaan ang number.
while True:
    # 4. Humingi ng input sa user
    guess = input("Hulaan mo ang number (1–100): ")

    # 5. Error checking
    # .isdigit() → chine-check kung lahat ng character ay digit (0–9).
    # Kung hindi number ang nilagay ng user, magbibigay tayo ng warning
    # at magpapatuloy lang ang loop (hindi babagsak yung program).
    if not guess.isdigit():
        print("❌ Oops! Kailangan number lang ang ilagay.")
        continue  # balik sa umpisa ng loop

    # 6. Convert string → integer
    # Lahat ng input() sa Python ay string by default.
    # Kaya kailangan natin gawing int para makumpara sa secret_number.
    guess = int(guess)

    # 7. Gamit ng if / elif / else para sa decision making
    if guess < secret_number:
        print("📉 Ang hula mo ay MABABA. Subukan ulit!")
    elif guess > secret_number:
        print("📈 Ang hula mo ay MATAAS. Subukan ulit!")
    else:
        # Kapag wala sa less-than o greater-than, ibig sabihin TAMA!
        print("🎉 Tama ka! Ang number ay:", secret_number)

        # 8. break → tatapusin na ang loop
        # Dahil nakuha na ang tamang sagot, ayaw na nating ipagpatuloy.
        break
