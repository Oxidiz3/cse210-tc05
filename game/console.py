
class Console():
	'''The Console class takes input from the user and
	prints strings to the console
	'''
	def get_letter(self) -> str:
		'''Gets input from the user

		Returns:
			str: Users guess
		'''
		guess = input("Guess a letter [a-z]: ")
		return guess

	def print(self, print_string: str):
		'''Takes string and prints it to the console

		Args:
			print_string (str): the string to be printed
		'''
		print(print_string)