from lib import Game

help = """
Enter:
Word List - print all the words I have found
Shuffle Letters - shuffle the game letters
Help - command list
Quit - quit game

Anything else to guess a word!
"""

def main():
    game = Game()
    
    print('\nWelcome to Reading Rainbow!')
    print(help)
    
    while True:
        print('Letters: ' + game.getLetters())
        command = input('Input: ').lower()
        
        if command == 'quit':  # Quit the game
            confirm = input('\nAre you sure you want to quit? (y/n): ').lower()
            if confirm == 'y':
                print("\nThanks for playing!\n")
                break
            else:
                print()
                continue
        elif command == 'help':  # Bring up the help text
            print(help)
            continue
        elif command == 'word list':  # Show me the words I have found
            print('\n', game.getFoundWords(), '\n')
            continue
        elif command == 'shuffle letters':  # Shuffle the non-center letters
            game.shuffle()
            print()
            continue
        elif len(command) < 4:  # Check for guesses that are too short
            print('\nNot enough letters!\n')
            continue
        elif game.getCenterLetter() not in command:  # Check if the guess has the center letter
            print('\nMust contain center letter!\n')
            continue
        elif not set(command).issubset(set(game.getPangram())):  # Check that all input characters are part of the letter set
            print('\nSome characters not allowed!\n')
            continue
        elif command in game.getFoundWords():  # Check to see if I have already found the input guess
                print('\nAlready found this word!\n')
        else:  # Otherwise, guess is valid word that has not been guessed before
            game.setFoundWord(command)
            print()

        if len(game.getFoundWords()) == len(game.getGameWords()): # Check to see if all words have been found
            print('\nQueen bee! You found all the words and won the game!\n')
            break

main()