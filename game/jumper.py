#Weston Ford
#class: CSE 210
#instructor: Adam Hayes

class Jumper:
    def __init__(self): 
        self.guess_line = '_ _ _ _ _'
        self.parachute = (
'''
  ___  
 /___\ 
 \   / 
  \ /  
   0   
  /|\  
  / \  

^^^^^^^
'''
        )
    
    def draw(self):
        print(self.guess_line)
        print(self.parachute)

    def check_line(self):
        self.is_incomplete = False
        self.index = 0
        while self.is_incomplete == False and self.index < len(self.guess_line):
            if self.guess_line[self.index] == '_':
                self.is_incomplete = True
            else:
                self.index += 1
        return self.is_incomplete
    
    def insert_letter(self, guess, index):
        index = (index-1)*2
        line = self.guess_line

        self.guess_line = line[:index] + guess + line[index+1:]
    
    def cut_line(self):
        if self.parachute == (
'''
   0   
  /|\  
  / \  

^^^^^^^
'''
        ):
            self.parachute = (
'''
   x   
  /|\  
  / \  

^^^^^^^
'''
            )
        else:
            self.parachute = self.parachute[8:]
