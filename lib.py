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
    _messages = {'length': '\nNot enough letters!\n', 'center_letter': '\nMust contain center letter!\n', 'invalid_chars': '\nSome characters not allowed!\n', 'found_word': '\nAlready found this word!\n', 'queen_bee': '\nQueen bee! You found all the words and won the game!\n', 'new_word': '\nCongrats! You found a word!: ', 'invalid_word': '\nNot a legal word!\n'}

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

