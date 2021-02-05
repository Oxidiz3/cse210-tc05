import random

class word():

    def word_list(self):
        words = ['dream', 'laugh', 'apple', 'tiger', 'seven', 'world', 'sugar', 'women', 'mouth', 'music']
        return words

    def select_word(self, words):
        word = random.choice(words)
        return word

    def check_letter(self, word, guess):
        if word.index(guess) != -1:
            return "not found"
        else:
            return word.index(guess)