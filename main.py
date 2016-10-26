#File: main.py
#This file runs the program for the main.ai coding challenge
#Annie Ritch, 10-26-16
#python 2.7.12

import functions

inputFile = 'smaller.dat' #input data file
sigma = 4 #support level parameter (min. frequency of item set occurrence)
outputFile = 'smaller_results.dat'


functions.writeCoOccurrenceOutput(inputFile, sigma, outputFile)