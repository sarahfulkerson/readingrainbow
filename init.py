from lib import select_pangram, select_center_letter, generate_game_words

pangram = select_pangram()
center_letter = select_center_letter(pangram)
generate_game_words(pangram)
print(pangram, center_letter)