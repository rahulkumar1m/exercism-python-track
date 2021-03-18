import random
from string import ascii_lowercase as letters
from itertools import cycle

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = "".join(random.choice(letters) for _ in range(100))
        else:
            self.key = key

    def encode(self, text: str):
        encoded = []
        for ch1, ch2 in zip(text, cycle(self.key)):
            encoded.append(letters[(ord(ch1) % 97 + ord(ch2) % 97) % 26])
        return "".join(encoded)


    def decode(self, text: str):
        decoded = []
        for ch1, ch2 in zip(text, cycle(self.key)):
            decoded.append(letters[(ord(ch1) % 97 - ord(ch2) % 97) % 26])
        return "".join(decoded)
