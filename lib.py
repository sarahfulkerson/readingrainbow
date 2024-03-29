import pickle
import random

def loadSavedGame():
    file = open('savedGame', 'rb')
    savedGame = pickle.load(file)
    file.close()

    return savedGame

def saveGame(game):
    file = open('savedGame', 'wb')
    pickle.dump(game, file)
    file.close()

class Game():
    _messages = {'length': '\nNot enough letters!', 
                 'center_letter': '\nMust contain center letter!', 
                 'invalid_chars': '\nSome characters not allowed!', 
                 'found_word': '\nAlready found this word!', 
                 'queen_bee': '\nQueen bee! You found all the words and won the game!', 
                 'new_word': '\nCongrats! You found a word!: ', 
                 'invalid_word': '\nNot a legal word!',
                 'save': '\nProgress saved!'}

    def __init__(self):
        self.pangram = self.setPangram()
        self.center_letter = self.setCenterLetter()
        self.game_words = self.setGameWords()
        self.letters = self.setLetters()
        self.found_words = []

    def setPangram(self):
        pangrams_file = open('pangrams.txt','r').readlines()
        return pangrams_file[random.randint(0,len(pangrams_file)-1)].strip()
    
    def setCenterLetter(self):
        center_letter = [*set([*self.getPangram()])]
        return center_letter[0]
    
    def setGameWords(self):
        wordlist_file = open('wordlist.txt','r')
        gameWords = []

        for word in wordlist_file:
            word_set = set(word.strip())
            
            if word_set.issubset(set(self.getPangram())) and self.getCenterLetter() in word:
                gameWords.append(word.strip())

        wordlist_file.close()
        return gameWords
    
    def setLetters(self):
        return ''.join([self.getCenterLetter()] + [x for x in set(self.getPangram())-set(self.getCenterLetter())])
    
    def setFoundWord(self, command):
        self.found_words.append(command)
        
    def getPangram(self):
        return self.pangram
    
    def getCenterLetter(self):
        return self.center_letter
    
    def getGameWords(self):
        return self.game_words
    
    def getLetters(self):
        return self.letters
    
    def getFoundWords(self):
        return self.found_words

    def shuffle(self):
        other_letters = [x for x in self.letters[1:]]
        random.shuffle(other_letters)
        self.letters = self.getCenterLetter() + ''.join([x for x in other_letters])
    
    def printFoundWords(self):
        word_list = self.getFoundWords()
        word_string = ''

        word_list.sort()

        for word in word_list:
            word_string = word_string + word + ' '
        
        return word_string

    def printGrid(self):
        gameLetters = self.getLetters()
        grid = """
            ___   ___
           / %s \ / %s \\
           \___/ \___/
         ___   ___   ___
        / %s \ / %s \ / %s \\
        \___/ \___/ \___/
            ___   ___
           / %s \ / %s \\
           \___/ \___/
        """ % (gameLetters[1], gameLetters[2], gameLetters[3], gameLetters[0], gameLetters[4], gameLetters[5], gameLetters[6])
        return grid