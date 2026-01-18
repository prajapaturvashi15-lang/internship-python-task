import random

words = ["python", "intern", "coding", "program"]
word = random.choice(words)

guessed = []
attempts = 6

print("🎮 Welcome to Hangman Game")

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("⚠ Already guessed")
    elif guess in word:
        guessed.append(guess)
        print("✅ Correct guess")
    else:
        guessed.append(guess)
        attempts -= 1
        print("❌ Wrong guess. Attempts left:", attempts)

if attempts == 0:
    print("😢 Game Over! The word was:", word)