# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.characters = ''
        for char in self.word:
            self.characters = self.characters + '_'

    def guess(self, char):
        if self.status == STATUS_WIN or self.status == STATUS_LOSE:
            raise ValueError("Invalid Guess")
        elif char in self.word and char not in self.characters:
            cont = 0
            for c in self.word:
                if c == char:
                    self.characters = list(self.characters)
                    self.characters[cont] = char
                    self.characters == "".join(self.characters)
                cont += 1
        else:
            self.remaining_guesses -= 1            

    def get_masked_word(self):
        return "".join(self.characters)

    def get_status(self):
        if '_' not in self.characters:
            self.status = STATUS_WIN
        elif self.remaining_guesses <= 0:
            self.status = STATUS_LOSE

        return self.status
