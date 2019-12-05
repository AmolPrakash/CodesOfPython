import os
import random
import linecache

def print_board(wrong_guesses):
 boards = [""" 
    ____
   |    |     
        |
        |
        |
        |
        |
     =======	 
	""","""
    ____
   |    |     
   O    |
        |
        |
        |
        |
     =======	 
	""","""
    ____
   |    |     
   O    |
   |    |
        |
        |
        |
     =======	 
	""",
	"""
    ____
   |    |     
   O    |
   |/   |
        |
        |
        |
     =======	 
	""",
	"""
    ____
   |    |     
   O    |
  \|/   |
        |
        |
        |
     =======	 
	""",
	"""
    ____
   |    |     
   O    |
  \|/   |
   |    |
        |
        |
     =======	 
	""",
	"""
    ____
   |    |     
   O    |
  \|/   |
   |    |
  /     |
        |
     =======	 
	""",
	"""
    ____
   |    |     
   O    |
  \|/   |
   |    |
  / \   |
        |
     =======	 
	"""]
 print (boards[wrong_guesses])				 

def intro():
	username = raw_input('What\'s your name?\n')
	return username
 
def choose_word():
	f = open('words2.txt','r')
	line_number = random.randint(1, len(f.readlines()))
	word = linecache.getline('words2.txt', line_number)
	return word

def start_game():

	username = intro()
	print ('Welcome, %s! Let\'s play some fucking hangman.\n') % username
 
	word = choose_word()
	blanks = (len(word) - 1) * [' _ ']
	wrong_guesses = 0
	correct_guesses = 0
	guessed_letters = ''
	
	print_board(wrong_guesses)
	print (''.join(blanks))

	while wrong_guesses !=7 and correct_guesses != len(word) - 1:

		the_guess = raw_input('Guess a letter!\n')
		the_guess = the_guess.strip()
		the_guess = the_guess.lower()
	
		if the_guess == 'exit':
			break
			
		if len(the_guess) == 1 and the_guess.isalpha():		
			if guessed_letters.find(the_guess) != -1: 
				print ('Dipshit, you already guessed "%s"! You still have %d guesses left.') % (the_guess, 7 - wrong_guesses)			
			elif word.find(the_guess) == -1: 
				if wrong_guesses == 6:
					wrong_guesses = wrong_guesses + 1
					print_board(7)
					print ('SUCKS FOR YOU %s, YOU GOT FUCKING HANGED!\nTHE WORD WAS %s') % (username.upper(), word.upper())
				else:
					wrong_guesses = wrong_guesses + 1
					guessed_letters = guessed_letters + the_guess + ' '
					print ('Sorry, "%s" is not in the word. You have %d guesses left.') % (the_guess, 7 - wrong_guesses)   
			elif word.find(the_guess) != -1:
				for i in range(len(word) - 1):
					if the_guess == word[i]:
						correct_guesses = correct_guesses + 1
						blanks[i] = ' ' + the_guess + ' '
				if correct_guesses == len(word) - 1:
					print_board (wrong_guesses)
					print (''.join(blanks))
					print ('NICE JOB %s, YOUR SHITTY LIFE HAS BEEN SPARED!') % username.upper()
					break
				else:	
					print ('correct_guesses', len(word)-1	)	
					guessed_letters = guessed_letters + the_guess + ' '
					print ('Nice job! "%s" is in the word. You still have %d guesses left.') % (the_guess, 7-wrong_guesses)   
				
		print_board(wrong_gues0ses)
		print (''.join(blanks)	
		print ('Letters guessed: %s' % guessed_letters)
	
if __name__ == '__main__':
  start_game()
