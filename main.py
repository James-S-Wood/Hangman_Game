import random
import tkinter as tk
from tkinter import messagebox

"""This code uses the Tkinter library to create a simple GUI for the Hangman Game. The main game logic remains
 the same, but now the game interface is displayed in a window with interactive elements. The code creates a 
 window using tkinter.Tk(), adds labels to display the game title, the guessed word, and the number of tries 
 left. It also includes an entry field for the user to input their guesses and a button to check their guess.
"""


def hangman():
    words = ["python", "programming", "computer", "hangman", "openai"]
    selected_word = random.choice(words).lower()
    word_length = len(selected_word)
    tries = 6
    guessed_letters = []
    guessed_word = ["_"] * word_length

    def check_guess():
        guess = guess_entry.get().lower()
        guess_entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Guess", "Please enter a single letter.")
            return

        if guess in guessed_letters:
            messagebox.showinfo("Duplicate Guess", "You already guessed that letter. Try again.")
            return

        guessed_letters.append(guess)

        if guess in selected_word:
            for i in range(word_length):
                if selected_word[i] == guess:
                    guessed_word[i] = guess

            if "_" not in guessed_word:
                messagebox.showinfo("Congratulations", f"You guessed the word correctly: {selected_word}")
                window.destroy()
        else:
            nonlocal tries
            tries -= 1

            if tries == 0:
                messagebox.showinfo("Game Over", f"You ran out of tries. The word was: {selected_word}")
                window.destroy()
            else:
                # Update the gallows image based on the number of tries left
                gallows_canvas.itemconfigure(gallows_images[6 - tries], state=tk.NORMAL)

        update_game()

    def update_game():
        tries_label.config(text=f"Tries left: {tries}")
        guessed_word_label.config(text=" ".join(guessed_word))

    window = tk.Tk()
    window.title("Hangman")
    window.resizable(False, False)

    title_label = tk.Label(window, text="Hangman", font=("Arial", 24))
    title_label.pack(pady=10)

    gallows_canvas = tk.Canvas(window, width=200, height=200)
    gallows_canvas.pack()

    gallows_images = [
        gallows_canvas.create_line(20, 180, 180, 180, width=3, ),
        gallows_canvas.create_line(50, 180, 50, 20, width=3, ),
        gallows_canvas.create_line(50, 20, 130, 20, width=3, ),
        gallows_canvas.create_line(130, 20, 130, 50, width=3, ),
        gallows_canvas.create_oval(115, 50, 145, 80, width=3, ),
        gallows_canvas.create_line(130, 80, 130, 130, width=3, ),
        gallows_canvas.create_line(130, 100, 115, 120, width=3, ),
        gallows_canvas.create_line(130, 100, 145, 120, width=3, )
    ]

    for image in gallows_images:
        gallows_canvas.itemconfigure(image, state=tk.HIDDEN)

    word_label = tk.Label(window, text="Word:")
    word_label.pack()

    guessed_word_label = tk.Label(window, text=" ".join(guessed_word), font=("Arial", 16))
    guessed_word_label.pack()

    guess_label = tk.Label(window, text="Enter your guess:")
    guess_label.pack()

    guess_entry = tk.Entry(window, font=("Arial", 16))
    guess_entry.pack()

    check_button = tk.Button(window, text="Check", command=check_guess)
    check_button.pack(pady=10)

    tries_label = tk.Label(window, text=f"Tries left: {tries}")
    tries_label.pack()

    update_game()

    window.mainloop()


hangman()
