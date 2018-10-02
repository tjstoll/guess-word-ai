'''
'''

import re as re
import numpy as np

class Brain(object):
    """  """
    
    def __init__(self, nLets):
        '''
        '''
        self.next_guess = 'A'
        self.previous_guesses = 'A'
        self.nLets = nLets
        self.partial_word = '.'*nLets
        
        file = open('words.txt', 'r')
        self.words = [line.strip('\n') for line in file if len(line.strip('\n')) == nLets]
        file.close()
        
# -----------------------------------------------------------------------------
    def emitGuess(self):
        '''
        Uses the narrowed list of words and partial word to generate a unique
        guess
        '''
        if len(self.words) > 0:
            guess = self.words[0][0]
            i = 1
            while guess.upper() in self.previous_guesses and i <= self.nLets:
                guess = self.words[0][i]
                i+=1
            self.next_guess = guess.upper()
            self.previous_guesses += self.next_guess
            
        else:
            print('knowledge base depleted')
            letters = 'bcdefghijklmonpqrstuvwxyz'
            guess = letters[0]
            i = 1
            while i <= 25 and guess.upper() in self.previous_guesses:
                guess = letters[i]
                i+=1
            self.next_guess = guess.upper()
            self.previous_guesses += self.next_guess
        
# -----------------------------------------------------------------------------
    def buildPartial(self, letter_pos):
        '''
        Builds a partial word out of the correctly guessed letter and postion
        '''
        string = ''
        
        for i in range(self.nLets):
            if i in letter_pos:
                string += self.next_guess.lower()
            elif self.partial_word[i] != '.':
                string += self.partial_word[i]
            else:
                string += '.'
        return string
            
# -----------------------------------------------------------------------------
    def cleanList(self, correct, letter_pos):
        '''
        Take in the correct or incorrect guess and clean the list of words
        accordingly.
        This call results in a narrowed list of possible words and a more
        populated partial word
        '''
        # Process out all the words that do not contain the letter pattern
        if correct:
            # Build the partial word
            self.partial_word = self.buildPartial(np.array(letter_pos)-1)
            lst = [] # To hold matches
            # Look for matches and build new list
            for line in self.words:
                if re.match(self.partial_word, line):
                    lst.append(line)
                else:
                    pass
            self.words = lst
        
        # Process out all the words that contain the letter
        else:
            lst = []
            for line in self.words:
                if self.next_guess.lower() in line:
                    pass
                else:
                    lst.append(line)
            self.words = lst
                    