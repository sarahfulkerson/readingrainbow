from lib import Game
from lib import loadSavedGame, saveGame

help = """
Enter:
W (Word List) - print all the words I have found
S (Shuffle Letters) - shuffle the game letters
H (Help) - command list
A (Save Game) - save the progress of your current game
Q (Quit) - quit game

Anything else to guess a word!
"""

def main():
    game = Game()
    
    # Load a saved game or start a new one
    while True:
        print('\nWelcome to Reading Rainbow!\n\nWould you like to [start] a new game, [load] your last save, or [quit]?\n')
        command = input('Input: ').lower()
       
        if command == 'start':
            break
        elif command == 'load':
            try:
                game = loadSavedGame()
                break
            except FileNotFoundError:
                print('\n No saved game was found!')
                continue
        elif command == 'quit':
            print("\nThanks for playing!\n")
            exit()
        else:
            continue
        
    print(help)
    
    # Play the game
    while True:
        print(game.printGrid())
        print('Letters: ' + game.getLetters())
        command = input('Input: ').lower()

        # Quit the game
        if command == 'q':
            confirm = input('\nAre you sure you want to quit? (y/n): ').lower()
            if confirm == 'y':
                print('\nThanks for playing!\n')
                break
            else:
                print()
                continue

        elif  command == 't':
            print('\n', game.getGameWords())
            continue

        # Bring up the help text
        elif command == 'h':
            print(help)
            continue

        # Show me the words I have found
        elif command == 'w':
            print('\n', game.printFoundWords())
            continue
        
        # Shuffle the non-center letters
        elif command == 's':
            game.shuffle()
            print()
            continue

        # Save the progress of my current game
        elif command == 'a':
            saveGame(game)
            print(game._messages['save'])

        # Check for guesses that are too short
        elif len(command) < 4:
            print(game._messages['length'])
            continue
        
        # Check if the guess has the center letter
        elif game.getCenterLetter() not in command:
            print(game._messages['center_letter'])
            continue

        # Check that all input characters are part of the letter set
        elif not set(command).issubset(set(game.getPangram())):
            print(game._messages['invalid_chars'])
            continue

        # Check to see if I have already found the input guess
        elif command in game.getFoundWords():
                print(game._messages['found_word'])

        # Otherwise, guess is valid word that has not been guessed before   
        else:
            if command in game.getGameWords():
                game.setFoundWord(command)
                print(game._messages['new_word'] + command)
            else:
                print(game._messages['invalid_word'])

        # Check to see if all words have been found
        if len(game.getFoundWords()) == len(game.getGameWords()):
            print(game._messages['queen_bee'])
            break

main()