from console import Console
from word import word
from jumper import Jumper

#Zach Wilson
#Class: CSE 210
#Instructor: Adam Hayes

class Director():

	'''The Director class imports all the other classes and
	   directs the flow of the game.'''
	
	def __init__(self):

		'''Intializes the variables for the class.'''
		
		#Intializes the classes.
		self.console = Console()
		self.word = word()
		self.jumper = Jumper()

		#Intializes the global variables for the director class.
		self.keep_playing = True
		self.secret_word = self.word.select_word(self.word.word_list())
		self.guess = ''
		self.wrong_guess = 0
		
	def start_game(self):

		'''Starts the game.'''

		while self.keep_playing:
			self.get_input()
			self.do_update()
			self.do_output()
	
	def get_input(self):
		
		'''Prints off the word list and the jumper and gets the
		   user's input.'''

		self.jumper.draw()
		self.guess = self.console.get_letter()

	def do_update(self):
		
		'''Checks to see if the letter is in the word, and then
		   updates either the word list or the jumper.'''
		
		self.checker = self.word.check_letter(self.secret_word, self.guess)

		if isinstance(self.checker, int):
			self.jumper.insert_letter(self.guess, self.checker + 1)
		else:
			self.wrong_guess += 1
			self.jumper.cut_line()

	def do_output(self):
		if self.wrong_guess == 4:
			self.keep_playing = False
			self.jumper.cut_line()
			self.jumper.draw()
			print('Game over')
		elif self.jumper.check_line() == False:
			self.keep_playing = False
			print('You won!')
		else:
			pass
