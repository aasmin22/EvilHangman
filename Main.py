def getWords(fname, length):
    infile = open(fname)
    words = []
    for line in infile:
        line = line.strip()
        if len(line) == length:
            words.append(line)
    infile.close()
    return words


def displayListAsString(lst):
    lString = str(lst)
    print(lString)


def getLocations(letter, word):
    index = []
    for i in range(len(word)):
        if word[i] == letter:
            index.append(i)
    return index


def mostFrequent(wordFamilies):
    longest = 0
    fewestBlanks = 0
    longestKey = ""
    for k, v in wordFamilies.items():
        if len(v) > longest:
            longest = len(v)
            fewestBlanks = k.count("-")
            longestKey = k
        elif len(v) == longest:
            numBlanks = k.count("-")
            if numBlanks < fewestBlanks:
                fewestBlanks = numBlanks
                longestKey = k
            elif numBlanks == fewestBlanks and letter in k:
                longestKey = k
    return longestKey


def partition(wordList, letter):
    patterns = {}
    for word in wordList:
        positions = getLocations(letter, word)
        pattern = ""
    for i in range(len(word)):
        if i in positions:
            pattern += letter
        else:
            pattern += "-"
    if pattern in patterns:
        patterns[pattern].append(word)
    else:
        patterns[pattern] = [word]

    return patterns


def evilHangman():
    length = int(input("Enter the length of a word: "))
    print("-=" * 30)
    wordList = getWords("CraWords.txt", length)
    tries = 99
    badGuesses = []
    guesses = []
    pattern = "-" * length
    wordFamilies = {pattern: wordList}

    while tries >= 0:
        pattern = mostFrequent(wordFamilies)

        print("You have: ", pattern)
        print("Bad Guesses: ", badGuesses)
        print("Guesses so far: ", guesses)

        if "-" not in pattern:
            print("You guessed the word!")
            break

        letter = input("Guess a letter: ").lower()
        print("-=" * 30)

        if letter in badGuesses or letter in guesses:
            print("The letter has been guessed! Try again")
            continue
        guesses.append(letter)

        if letter in pattern:
            positions = getLocations(letter, pattern)
            families = {}
            for word in wordFamilies[pattern]:
                key = ""
                for i in range(length):
                    if i in positions or word[i] == letter:
                        key += letter
                    else:
                        key += "-"
                if key in families:
                    families[key].append(word)
                else:
                    families[key] = [word]
            pattern = mostFrequent(families)
            wordFamilies = families
            print("Guessed letter is in the pattern!")
        else:
            wordFamilies = partition(wordFamilies[pattern], letter)
            if len(wordFamilies) == 1:
                pattern = list(wordFamilies.keys())[0]
            else:
                badGuesses.append(letter)
            print(wordFamilies)

        tries -= 1


evilHangman()