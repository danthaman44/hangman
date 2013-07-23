'''
Created on Mar 9, 2013

@author: weideng
'''

import UtilityFunctions
import random
import operator
import csv
    
def playHangman(group): #allows the user to play hangman from console or command line
    word = group[0]
    numtries = group[1]
    print "You are allowed " + str(numtries) + " incorrect guesses"
    wrongcount = 0 #the number of wrong guesses so far
    wordnospaces = word.replace(' ', '') 
    wordnolines = wordnospaces.replace('\n', '')
    wordset = set(wordnolines) #the list of correct letters the user should be guessing
    guesswordset = set('') #the list of correct guesses the user has made
    allwordsguessed = set('') #the list of all the guesses the user had made
    letterset = set('ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    print '_'*len(word)
    input = raw_input('Guess a letter: ')
    guess = set(input) 
    while wrongcount < numtries and guesswordset != wordset:       
        if guess.issubset(letterset) == False or len(guess) != 1: #the user did not guess a letter
            input = raw_input('Letters only. Guess a letter: ')
            guess = set(input)    
        elif guess.issubset(wordset) == False: #the user did not guess a correct letter
            wrongcount += 1
            if wrongcount == numtries: #the user used up all their incorrect guesses
                print 'You are hung! Word was: ' + word + '.\n'
                return
            UtilityFunctions.give_information(input, allwordsguessed, word, guesswordset, numtries, wrongcount)
            UtilityFunctions.input = raw_input('No ' + input + '. Guess another letter: ')
            guess = set(input)     
        elif guess.issubset(wordset): #the user guessed a correct letter
            guesswordset.add(input)
            UtilityFunctions.give_information(input, allwordsguessed, word, guesswordset, numtries, wrongcount)    
            if guesswordset == wordset: #the user guessed all the letters in the word
                print "Congratulations!\n"
                return 
            input = raw_input('Correct. Guess another letter: ')
            guess = set(input)
###############################################################################################
def buildStrategy(word): #returns the sorted list of letters the AI will guess
    wordfile = open("full_dictionary.txt") 
    wordlen = len(word) #the length of the word we are trying to guess
    wordlist=[]
    for line in wordfile:
        newline = line.replace('\n','')
        if (len(newline) == wordlen):
            wordlist.append(newline) #wordlist now contains all the words in our dictionary with the same length as the word we want to guess
    occurences = {} #dictionary tracking each character to occurences
    for words in wordlist:
        for char in words:
            if char not in occurences:
                occurences[char] = 1
            else:
                occurences[char] = occurences[char] + 1
    sortedChars = sorted(occurences.iteritems(), key=operator.itemgetter(1)) # a list of tuples
    sortedChars.reverse()  #each tuple has a char and its # of occurences              
    return sortedChars #chars with most occurences come first, the AI will guess them first
 ###############################################################################################   
            
def autoPlayHangman(group): #an AI player will play hangman
    word = group[0]
    sortedChars = buildStrategy(word) #the list of letters the AI will guess, with more common letters coming first
    index = 0 #index will increase as we move through sortedChars
    numtries = group[1]
    print "AI is allowed " + str(numtries) + " incorrect guesses"
    wrongcount = 0
    wordnospaces = word.replace(' ', '')
    wordnolines = wordnospaces.replace('\n', '')
    wordset = set(wordnolines)
    guesswordset = set('')
    allwordsguessed = set('')
    letterset = set('ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    print '_'*len(word)
    input = sortedChars[index][0]
    #print ("AI guessing: " + input +"\n")
    guess = set(input) 
    while wrongcount < numtries and guesswordset != wordset:
        print ("AI guessing: " + input)            
        if guess.issubset(letterset) == False or len(guess) != 1:
            input = raw_input('Letters only. Guess a letter: ')
            guess = set(input)    
        elif guess.issubset(wordset) == False:
            wrongcount += 1
            if wrongcount == numtries:
                print 'AI is hung! Word was: ' + word + '.\n'
                return
            UtilityFunctions.give_information(input, allwordsguessed, word, guesswordset, numtries, wrongcount)
            print("AI was wrong. AI will guess another letter\n")
            index+=1
            if index == len(sortedChars): #if 
                print 'AI is stumped! Word was: ' + word + '.\n'
                return
            input = sortedChars[index][0]
            guess = set(input)     
        elif guess.issubset(wordset):
            guesswordset.add(input)
            UtilityFunctions.give_information(input, allwordsguessed, word, guesswordset, numtries, wrongcount)    
            if guesswordset == wordset:
                print "AI has beaten hangman! To play again, chose a file\n"
                return 
            print("AI guessed correctly. AI will guess another letter\n")
            index +=1
            if index == len(sortedChars): #if 
                print 'AI is stumped! Word was: ' + word + '.\n'                 
                return
            input = sortedChars[index][0]
            guess = set(input) 
     
             
def executeHangman(): #the main method, runs the game
    while 1 > 0: #loops the game infinitely unless the user wants to quit
        file = csv.reader(open("words.csv", "rU"), dialect=csv.excel_tab)
        newlist = UtilityFunctions.formatHangmanData(file)
        word = UtilityFunctions.create_word(newlist)
        whichMode = int(raw_input("User or AI game? (0 for User, 1 for AI) ")) #0 for user, 1 for AI
        if whichMode == 0:
            playHangman(word)
            cont = raw_input('Type y to play again. Type n to quit\n ')
            if (cont == 'n'):
                return
        elif whichMode == 1:
           autoPlayHangman(word)
           cont = raw_input('Type y to play again. Type n to quit\n ')
           if (cont == 'n'):
                return
        word = UtilityFunctions.create_word(newlist)
 

def printCSV(): #handy function to view the contents of your csv
    file = csv.reader(open("words.csv", "rU"), dialect=csv.excel_tab)
    for row in file:
       print row



print executeHangman()


    
    