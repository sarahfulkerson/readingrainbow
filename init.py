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
        
        # Quit the game
        if command == 'quit':
            confirm = input('\nAre you sure you want to quit? (y/n): ').lower()
            if confirm == 'y':
                print("\nThanks for playing!\n")
                break
            else:
                print()
                continue

        # Bring up the help text
        elif command == 'help':
            print(help)
            continue

        # Show me the words I have found
        elif command == 'word list':
            print('\n', game.getFoundWords(), '\n')
            continue
        
        # Shuffle the non-center letters
        elif command == 'shuffle letters':
            game.shuffle()
            print()
            continue

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
            game.setFoundWord(command)
            print()

        # Check to see if all words have been found
        if len(game.getFoundWords()) == len(game.getGameWords()):
            print(game._messages['queen_bee'])
            break

main()