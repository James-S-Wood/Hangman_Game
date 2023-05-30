import random

def hangman():
    words = ["python", "programming", "computer", "hangman", "openai"]
    selected_word = random.choice(words).lower()
    word_length = len(selected_word)
    tries = 6
    guessed_letters = []
    guessed_word = ["_"] * word_length

    print("Welcome to Hangman!")
    print("Guess the word by entering one letter at a time.")
    print("You have 6 tries to guess the word correctly.")

    while tries > 0:
        print("\n")
        print(" ".join(guessed_word))
        print("Tries left:", tries)

        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in selected_word:
            for i in range(word_length):
                if selected_word[i] == guess:
                    guessed_word[i] = guess

            if "_" not in guessed_word:
                print("\nCongratulations! You guessed the word correctly:", selected_word)
                return
        else:
            tries -= 1
            print("Wrong guess. Try again.")

    print("\nGame over! You ran out of tries.")
    print("The word was:", selected_word)

hangman()
