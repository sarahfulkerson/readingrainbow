import random

class Game():
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
        gamewordlist = []

        for word in wordlist_file:
            word_set = set(word.strip())
            
            if word_set.issubset(set(self.getPangram())) and self.getCenterLetter() in word:
                gamewordlist.append(word.strip())

        wordlist_file.close()
        return gamewordlist
    
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