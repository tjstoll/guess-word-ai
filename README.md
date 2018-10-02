# Guess Word (Pseudo) AI
###An AI approach to the reversal of the popular 'Hang Man' game. 

## As of now...
...it is a console-based python game similar to the [Guess Word](https://github.com/tjstoll/guess-word) game I created a few years ago. The only difference is that the program has to guess what word *you* are thinking of.

## How Do I Play?
It's so easy!
1. Make sure you have a Python 3 IDE istalled
2. Copy the files as they are named into a directory on your machine
3. Open the `index.py` in your IDE and press the run button
4. Follow the program's instructions

Here are some gameplay functionality notes:
Your game might look like this if you're thinking of the word 'AARDVARK':
```python
Next Guess: A
_ _ _ _ _ _ _ _
1 2 3 4 5 6 7 8
Previous Guesses: PQ
Total Strikes: 2

Correct Guess (y/n)? y
Letter Location(s): 1,2,4
```
- To indicate where a letter goes input the positions as `1` or `3,6` or `12,1,3` and so on (order does not matter). In this case, you would input `1,2,4`
- To leave the game input the word `exit` when the program asks to validate its guess

## Plans For The Future
As you may have noticed, this is very rough. The "database" is a simple `.txt` file, the UI is the console, and the program will crash if its knowledge base is surpassed. However, in the future these and other things will change, such as:
- This project will be brought to the web
- A SQL database will be used to hold information about words and basic user habits
- A real UI will be designed to make the game more attractive
- A more robust guessing algorithm will be developed to make the program smarter
And down the line I hope to use the data collected in this project to create another project in the realm of Data Science.

As always, comments, concern, and constructive critism is gladly welcomed! Send them to [taneisha@tjstoll.com](mailto:taneisha@tjstoll.com?Subject=Guess%20Word%20AI%20Comments)