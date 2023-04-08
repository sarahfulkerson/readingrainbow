import random

def puzzle_letters():
    vowels = {'a','e','i','o','u','y'}
    consonants = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'}

    puzzle_letters = []
    
    puzzle_letters.append(vowels.pop())
    puzzle_letters.append(vowels.pop())
    puzzle_letters.append(consonants.pop())
    puzzle_letters.append(consonants.pop())
    puzzle_letters.append(consonants.pop())
    puzzle_letters.append(consonants.pop())
    puzzle_letters.append(consonants.pop())

    random.shuffle(puzzle_letters)

    return puzzle_letters

print(puzzle_letters())