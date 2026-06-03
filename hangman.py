import random

words = ["python", "apple", "banana", "coding", "computer"]

word = random.choice(words)

guessed = []

attempts = 6

while attempts > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 You Won!")
        break

    guess = input("Enter a letter: ").lower()

    guessed.append(guess)

    if guess not in word:
        attempts -= 1
        print("Wrong Guess!")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("Game Over!")
    print("The word was:", word)