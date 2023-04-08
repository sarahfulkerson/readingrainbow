
wordlist = open('wordlist.txt', 'w')

for line in open('word.lst'):
    chars = set([*line.strip()])

    if len(line.strip()) > 3 and len(chars) < 8 and 's' not in chars: 
        wordlist.write(line)

wordlist.close()