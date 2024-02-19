from models import Word,WordPoolModel
from connect import SessionLocal
import random

def fetch_word_pool():
    session = SessionLocal()
    words = session.query(Word).all()
    session.close()
    return words

class GameView:
    def display_intro(self):
        print("Welcome to the Word Guessing Game!")

    def display_start_message(self, rating):
        print(f"Starting a {rating} word.")

    def display_blank_rectangles(self):
        print("[ ] [ ] [ ] [ ] [ ]")

    def display_invalid_guess(self):
        print("Invalid guess! Please enter exactly 5 letters.")

    def display_guess_result(self, correct_letters):
        print(f"Correct letters: {correct_letters}")

    def display_win_message(self):
        print("Congratulations! You win!")

    def display_lose_message(self, word):
        print(f"Sorry, you lose. The correct word was {word}.")

    def color_rectangle(self, idx, color):
        if color == "green":
            print(f"[\033[92m{idx}\033[0m]", end=" ")
        elif color == "yellow":
            print(f"[\033[93m{idx}\033[0m]", end=" ")
        else:
            print(f"[ {idx} ]", end=" ")

    def add_blank_row(self):
        print()


class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.word = ""
        self.rating = ""
        self.guesses = 0

    def start_game(self):
        word_pool = self.model.fetch_word_pool()
        word = random.choice(word_pool)
        if len(word.word) != 5:
            raise ValueError("Word must be 5 letters long.")
        self.word = word.word
        self.difficulty = word.difficulty
        self.view.display_start_message(self.rating)
        self.view.display_blank_rectangles()
        
    def submit_guess(self, guess):
        if len(guess) != 5 or not guess.isalpha():
            self.view.display_invalid_guess()
            return

        self.guesses += 1
        correct_letters = 0
        for idx, letter in enumerate(guess):
            if letter == self.word[idx]:
                correct_letters += 1
                self.view.color_rectangle(idx, 'green')
            elif letter in self.word:
                self.view.color_rectangle(idx, 'yellow')
            else:
                self.view.color_rectangle(idx, 'black')

        # Add this line to print a new line after displaying the rectangles for the current guess.
        self.view.add_blank_row()

        if correct_letters == 5:
            self.view.display_win_message()
            self.start_game()
        elif self.guesses >= 5:
            self.view.display_lose_message(self.word)
            self.start_game()

    
if __name__ == "__main__":
    model = WordPoolModel()
    view = GameView()
    controller = GameController(model, view)
    controller.start_game()

    while True:
        guess = input("Enter your guess: ")
        controller.submit_guess(guess)