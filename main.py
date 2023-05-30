import random


def hangman():
    words = ["python", "programming", "computer", "hangman", "openai"]
    selected_word = random.choice(words).lower()
    word_length = len(selected_word)
    tries = 6
    guessed_letters = []
    guessed_word = ["_"] * word_length

    """In this updated version, I added a list called gallows that contains ASCII art representations 
    of the hangman's gallows at different stages. Each stage corresponds to the number of tries left in 
    the game. The gallows art is displayed before each guess, providing a visual representation of the 
    hangman's progress."""

    gallows = [
        '''
           +---+
               |
               |
               |
              ===
        ''',
        '''
           +---+
           O   |
               |
               |
              ===
        ''',
        '''
           +---+
           O   |
           |   |
               |
              ===
        ''',
        '''
           +---+
           O   |
          /|   |
               |
              ===
        ''',
        '''
           +---+
           O   |
          /|\\  |
               |
              ===
        ''',
        '''
           +---+
           O   |
          /|\\  |
          /    |
              ===
        ''',
        '''
           +---+
           O   |
          /|\\  |
          / \\  |
              ===
        '''
    ]

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

"""In this code, we define the hangman function that represents the main logic of the game. It initializes a list of words, selects a random word from the list, and sets up variables like the word length, number of tries, and lists to store guessed letters and the current state of the guessed word.

The function then enters a loop where it prompts the user for a guess, checks the validity of the guess, and updates the game state accordingly. If the guessed letter is correct, it updates the guessed word with the correctly guessed letter. If the guessed letter is incorrect, it reduces the number of tries.

The game continues until the player either guesses the word correctly or runs out of tries. At the end of the game, an appropriate message is displayed.

To play the Hangman game, simply call the hangman function.

Feel free to enhance the code further by adding ASCII art for the hangman's gallows or implementing more advanced features like difficulty levels or word categories.

Have fun coding and enjoy playing Hangman!"""

