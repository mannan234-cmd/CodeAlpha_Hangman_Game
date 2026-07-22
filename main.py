import random
from words import words

# Choose a random word

secret_word = random.choice(words)

# Game Variables

guessed_letters = []
wrong_guesses = 0
MAX_WRONG = 6

print("=" * 45)
print("         WELCOME TO HANGMAN ")
print("=" * 45)


# Main Game Loop

while True:

    # Build hidden word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    # Display Game Status
    print("\n" + "-" * 45)
    print("Word           :", display_word)
    print(f"Wrong Guesses  : {wrong_guesses}/{MAX_WRONG}")
    print("Guessed Letters:", " ".join(guessed_letters))
    print("-" * 45)

    # Win Condition
    if "_" not in display_word:
        print("\n Congratulations!")
        print("You guessed the word correctly.")
        print("The word was:", secret_word)
        break

    # Lose Condition
    if wrong_guesses >= MAX_WRONG:
        print("\n Game Over!")
        print("You ran out of guesses.")
        print("The word was:", secret_word)
        break

    # User Input
    guess = input("\nEnter a letter (or type 'quit' to exit): ").lower().strip()

    # Quit Game
    if guess == "quit":
        print("\n Thanks for playing!")
        break

    # Input Validation
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter exactly one alphabet letter.")
        continue

    # Already Guessed
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    # Save Guess
    guessed_letters.append(guess)

    # Check Guess
    if guess in secret_word:
        print(" Correct Guess!")
    else:
        wrong_guesses += 1
        print(" Wrong Guess!")