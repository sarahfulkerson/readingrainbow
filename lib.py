import random

def select_pangram():
    pangrams_file = open('pangrams.txt','r').readlines()

    return pangrams_file[random.randint(0,len(pangrams_file)-1)].strip()

def select_center_letter(pangram):
    center_letter = [*set([*pangram])]
    
    return center_letter[0]

def generate_game_words(pangram):
    wordlist_file = open('wordlist.txt','r')
    gamewordlist_file = open('gamewordlist.txt','w')

    for word in wordlist_file:
        word_set = set(word.strip())
        
        if word_set.issubset(set(pangram)):
            gamewordlist_file.write(word)


    wordlist_file.close()
    gamewordlist_file.close()