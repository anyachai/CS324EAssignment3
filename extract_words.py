def main():
    # Read input file and create list of all lines
    readFile = open('pg60646.txt', 'r')
    lines = readFile.readlines()

    # Create list of all words (with duplicates)
    allWords = allWordsListMaker(lines)

    # Write list of all words to "allwords.txt"
    writeToFile(allWords, "allwords.txt")

    # Create list of unique words (words that only appear once in text)
    uniqueWords = uniqueWordsListMaker(allWords)

    # Write list of all unique words to "uniquewords.txt"
    writeToFile(uniqueWords, "uniquewords.txt")


def allWordsListMaker(linesList):
    # Make wordlist
    wordlist = []

    #Traverse lines
    for line in linesList:
        #New word
        word = ''
        for x in range(len(line)):
            #Pull character from current line
            character = line[x]

            #If uppercase character, change it to lowercase
            if (64 < ord(line[x]) < 91):
                character = chr(ord(line[x]) + 32)

            #If lowercase character, add it to the current word, otherwise
            #   add current word to the allword list and reset the current word
            if ((96 < ord(character) < 123)):
                word = word + character

            else:
                # Only add a word to the current list if it's longer than 2 characters
                #   or it is the word a.
                if (word != '') and ((len(word) > 2) or (word == "a")):
                    wordlist.append(word)
                word = ''

        # Add last word on line to the wordlist
        if (word != '') and ((len(word) > 2) or (word == "a")):
            wordlist.append(word)

    # Return the wordlist
    return wordlist


def uniqueWordsListMaker(words):
    # Create two lists to find words that only appear once
    distinctWords = [] 
    duplicateWords = [] 

    for word in words:

        # Ignore words that have duplicates
        if word not in duplicateWords:

            # Label word as unique if it is not already
            if word not in distinctWords:
                distinctWords.append(word)

            # If it already labeled unique, then relabel is as not unique 
            else:
                distinctWords.remove(word)
                duplicateWords.append(word)

    return distinctWords


def writeToFile(wordList, fileName):
    # Open file
    writeFile = open(fileName, "w")

    # Traverse wordlist, add words to file
    for word in wordList[:-1]:
        writeFile.write(word + '\n')

    # Add last word without newline character
    writeFile.write(wordList[-1])

    # Close file
    writeFile.close()


if __name__ == '__main__':
    main()
