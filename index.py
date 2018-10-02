'''
GuessWordAI in Python...
Author: Taneisha Stoll
'''

import GameLoop

class Index(object):
    """ Entry and exit point """
    
    def __init__(self, name, nLets, category):
        '''
        name - name of player
        nLets - number of letters to be guessed
        category - word category
        '''
        self.player_name = name
        self.number_of_letters = nLets
        self.category = category

        gameLoop = GameLoop.GameLoop(name, nLets, category)        
    
if __name__ == '__main__':
    print("Hi I'm AnnieT1000. Imma guess whatever word you're thinking of.")
    name = input('Your name: ')
    numLets = input('Number of letters: ')
    cat = input('Category: ')
    
    game = Index(name, int(numLets), cat)