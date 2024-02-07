def main():
    # Read input file and create list of all lines
    readFile = open('pg60646.txt', 'r')
    lines = readFile.readlines()

    # Create list of all words (with duplicates)
    allWords = allWordsListMaker(lines)

    # Write list of all words to "allwords.txt"
    writeToAllWords(allWords)

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

def writeToAllWords(wordList):
    # Open file
    writeFile = open("allwords.txt", "w")

    # Traverse wordlist, add words to file
    for x in range(len(wordList)):

        # If at the end of the list just add the current word. Otherwide, add word plus a newline
        if (x == (len(wordList) - 1)):
            writeFile.write(wordList[x])
        else:
            writeFile.write(wordList[x] + '\n')

    # Close file
    writeFile.close()

main()
