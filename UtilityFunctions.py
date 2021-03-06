'''
Created on Mar 10, 2013

@author: weideng
'''
import random
import operator
import csv

def formatHangmanData(file): #takes a file object and returns a list of the lines in that file
    newlist=[]
    for line in file:
        newlist.append(line)
    return newlist #newlist is a list of lists

def printTheword(line, lettersguessed): #used for visually displaying which letters the user guessed correctly, and which spaces remain blank
    theword = ''
    for letter in line:
        if set(letter).issubset(lettersguessed):
                theword += letter
        else:
                theword +='_'
    print theword

def give_information(input, allwordsguessed, word, guesswordset, numtries, wrongcount): #gives user information about how many guesses they have left, and which letters they have already guessed
     allwordsguessed.add(input)
     allwordsguessed = sorted(allwordsguessed)
     printTheword(word, guesswordset)
     print 'Misses left: ' + str(numtries-wrongcount)
     lettersGuessed = ' '
     for item in allwordsguessed:
        lettersGuessed += item + ' '   
     print 'Letters guessed: ' + lettersGuessed 

def create_word(list): #randomly selects line in the list generated by formatHangman data
     randomInt = random.randint(0, len(list)-1)
     group = list[randomInt] 
     word = group[0]
     word = word.lower()
     num = group[1]
     num = int(num)
     group = [word, num]
     return group
 