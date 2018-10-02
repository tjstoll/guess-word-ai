
class Face(object):
    """ Builds the Face object """
    
    def __init__(self, nLets):
        '''
        '''
        self.game_board = ['_' for i in range(nLets)]
        self.number_of_letters = nLets
        
        
    def buildBoard(self, letterpos):
        '''
        Return the board
        board - list of letters and spaces
        letterpos - index 0: letter; index n: letter position
        '''
        board_string = ''
        pos_string = ''
        
        if letterpos != []:
            for i in range(1, len(letterpos)):
                self.game_board[letterpos[i]-1] = letterpos[0]
        
        for j in range(self.number_of_letters):
            # Build board for letters before 10
            if j != self.number_of_letters:
                if j < 9:
                    board_string += '{} '.format(self.game_board[j]) 
                    pos_string += '{} '.format(j+1)
                else:
                    board_string += '{}  '.format(self.game_board[j]) 
                    pos_string += '{} '.format(j+1)
                    
            # Build board for letter after 9
            else:
                board_string += self.game_board[j]
                pos_string += str(j+1)
                
        return board_string + '\n' + pos_string
    
        
    def gameState(self, next_guess, previous_guesses, strikes, letterpos):
        '''
        next_guess - next guess from the brain class
        previous_guesses - string of previous guess from brain class
        strikes - number of strikes from gameLoop
        
        Print the gameboard and all of its information.
        '''
        game_state = 'Next Guess: {}\n'.format(next_guess)
        board = self.buildBoard(letterpos)
        game_info = '\nPrevious Guesses: {}\nTotal Strikes: {}'.format(previous_guesses, strikes)
        
        game_state += board + game_info
        print(game_state)
        #user_response = input('Correct Guess (y/n)? ') # I feel like this should be in the gameLoop..
        
        #return None
        
        
    
    