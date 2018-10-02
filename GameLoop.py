'''

'''

import Face
import Brain

class GameLoop(object):
    """  """
    
    def __init__(self, name, nLets, category):
        '''
        Initialize the game by creating the Face and Brain objects and
        activating the game loop.
        name and category are meta data sent to the brain to store in the
        Memory database.
        nLets is passed to the Face to build the game and also to Brain to
        sort a list of possible words.
        '''
        self.name = name
        self.number_of_letters = nLets
        self.category = category
        
        self.brain = Brain.Brain(nLets)
        self.face = Face.Face(nLets)
        
        self.strikes = len(self.brain.previous_guesses)
        self.previous_guesses = self.brain.previous_guesses
        self.next_guess = self.brain.next_guess
        
        self.face.gameState(self.next_guess, self.previous_guesses, self.strikes, [])
        self.requestResponse()

# -----------------------------------------------------------------------------
    def requestResponse(self):
        '''
        Request the standard response from the user.
        '''
        user_input = input('Correct Guess (y/n)? ')
        self.validateResponse(user_input)
    
# -----------------------------------------------------------------------------
    def validateResponse(self, user_input):
        '''
        Make sure the response fits the valid response types. Ask again for
        valid input otherwise.
        '''
        
        if user_input == 'y':
            self.correctGuess()
            
        elif user_input == 'n':
            self.wrongGuess()
            
        elif user_input == 'exit':
            print("Thanks for playing!")
            return None
        
        else:
            # ask again for input
            user_input = input("Invalid input. Try again: ")
            self.validateResponse(user_input)
            
# -----------------------------------------------------------------------------
    def correctGuess(self):
        '''
        Submit the letter positions to the Face and Game
        '''
        
        # Put the letter in the correct position based on user input
        letterpos = [self.brain.next_guess]  # List to hold guess and letter positions
        _pos = input('Letter location(s): ') # Ask user for letter positions
        pos = _pos.split(',')                # Clean up input
        
        for p in pos:
            if int(p)-1 >= self.number_of_letters:
                print('Position {} does not exist. Please retype the letter positions.'.format(p))
                self.correctGuess()
                return None
            else:
                letterpos.append(int(p))
        
        # Send letterpos to Brain to deal with
        self.brain.cleanList(True, letterpos[1:])
        # Obtain next guess
        self.brain.emitGuess()
        
        # Check if the game is won
        
        self.face.gameState(self.brain.next_guess, self.brain.previous_guesses, self.strikes, letterpos)
        self.requestResponse()

# -----------------------------------------------------------------------------      
    def wrongGuess(self):
        '''
        Send the information to the Brain
        '''
        # Tell the brain that the letter or word guessed is incorrect
        self.brain.cleanList(False, [])
        # Obtain the next guess
        self.brain.emitGuess()
        
        # Update strikes
        self.strikes += 1
        
        self.gameStatus()
        
        self.face.gameState(self.brain.next_guess, self.brain.previous_guesses, self.strikes, [])
        self.requestResponse()
        
# -----------------------------------------------------------------------------
    def gameStatus(self):
        '''
        Check to make sure the game is still valid
        '''
        if self.strikes >= 26:
            print("Darn it I've lost! But I'm still learning.")
            word = input('What was the word? ')
            
            # Check if the word fits the number of letters and guessed letters and spelling
            if len(word) != self.number_of_letters:
                return "Word length does not match number of letters to be guessed" 
            # Save the word in memory
        return "Thanks for playing!"
        
        # Check if the game board is full of letters
        
# =============================================================================        
#if __name__ == '__main__':
#    gl = GameLoop('Taneisha', 5, 'cats')