import random

class word():

    def word_list(self):
        words = ['dream', 'laugh', 'phone', 'tiger', 'horse', 'world', 'sugar', 'women', 'mouth', 'music']
        return words

    def select_word(self, words):
        word = random.choice(words)
        return word

    def check_letter(self, word, guess):
        
        does_exist = False
        index = 0
        while does_exist == False and index < len(word):
            if word[index] == guess:
                does_exist = True
            else:
                index += 1
        
        if does_exist == False:
            return "not found"
        else:
            return index