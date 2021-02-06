from console import Console


class Director():

	'''The Director class imports all the other classes and
	   directs the flow of the game.'''
	
	def __init__(self):

		'''Intializes the variables for the class.'''
		
		#Intializes the classes.
		self.console = Console()
		'''
		self.word = Word()
		self.jumper = Jumper()
		'''

		#Intializes the global variables for the director class.
		self.keep_playing = True
		'''
		self.secret_word = self.word.select_word()
		'''
		self.guess = ''
		self.wrong_guess = 0
		self.word_list = ['_', '_', '_', '_', '_']
		self.jumper_list = ["   ___", r"  /___\ ", r"  \   / ", r"   \ / ", "    0", r"   /|\ ", r"   / \ ", "", " ^^^^^^^"]
	
	def start_game(self):

		'''Starts the game.'''

		while self.keep_playing:
			self.get_input()
			self.do_update()
			self.do_output()
	
	def get_input(self):
		
		'''Prints off the word list and the jumper and gets the
		   user's input.'''

		for letter in self.word_list:
			print(letter, end=' ')
		print('' * 2)
		self.display_jumper(self.jumper_list)
		print('')
		self.guess = self.console.get_letter()
		print('')

	def do_update(self):
		
		'''Checks to see if the letter is in the word, and then
		   updates either the word list or the jumper.'''
		
		self.checker = self.word.check_char(self.secret_word, self.guess)

		if self.checker >= 0:
			self.word_list[self.checker] = self.guess
		else:
			self.wrong_guess += 1
			self.jumper_list[0] = ''

	def do_output(self):
		if self.wrong_guess == 4:
			self.keep_playing = False
			self.jumper_list[0] = "    X"
			self.display_jumper(self.jumper_list)
		else:
			pass

	def display_jumper(self, jump_list):
		for part in jump_list:
			self.console.print(part)

director = Director()

director.get_input()