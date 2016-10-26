#File: functions.py
#This file contains helper functions used for mode.ai coding challenge
#Annie Ritch, 10-26-16
#python 2.7.12


#findAllSublists: function to get all possible sublists of a list
# INPUTS:
#    numList: list of integers
# OUTPUT:
#    generator object containing all possible sublists of input numList
#
#   This is a recursive approach that finds all subsets EXCLUDING a given
#element, then later adds subsets containing the originally excluded element
#to the overall set of subsets. The subsets are represented in a generator object
#in an attempt to save memory.
#   This function runs rather slowly for the scale of data contained in retail_25k.dat.
def findAllSublists(numList):

	if len(numList) <= 1:
		yield numList
		yield []
	else:
		for element in findAllSublists(numList[1:]):
			yield [numList[0]] + element
			yield element


#makeFrequencyDict: function that creates dictionary of set frequencies
# INPUTS:
#    filename (string): name of datafile to read
#    minSetSize (int): mininum number of items in a frequent item set (default: 3)
# OUTPUT:
#    dictionary with tuples (of item IDs) as keys, and frequency of tuple occurrence (int) as value
def makeFrequencyDict(filename, minSetSize = 3):
	file = open(filename)
	frequencyDict = {} #dictionary of integer tuples (of item IDs)

	#for each line in file, extract frequent item sets
	while True:
		line = file.readline()
		if line == '':
			break #end of file; stop reading

		# parse input text: make each line a list of integers
		lineNums = [int(n) for n in line.split()]
		if len(lineNums) >= minSetSize:  #consider only if enough items listed
			sublists = findAllSublists(lineNums)

			#consider only sublists of adequate size:
			for sublist in sublists:
				if len(sublist) >= minSetSize:
					#convert to tuple (lists aren't hashable), add to dictionary
					numTuple = tuple(sublist)
					if numTuple not in frequencyDict:
						frequencyDict[numTuple] = 1
					else:
						frequencyDict[numTuple] += 1

	return frequencyDict


#writeCoOccurrenceOutput: function to write output from frequency table to file
# INPUTS:
#    filename (string): name of datafile to read
#    sigma (int): 'support level' parameter, minimum frequency required
#    outFilename(string): name of datafile in which to write output
#    minSetSize(int): mininum number of items in a frequent item set (default: 3)
# OUTPUT:
#    file of frequent item sets with lines of the format:
#        <item set size (N)>, <co-occurrence frequency>, <item 1 id >, <item 2 id>, ... <item N id>
def writeCoOccurrenceOutput(filename, sigma, outFilename, minSetSize = 3):
	outfile = open(outFilename, 'w')

	#generate frequency dictionary
	frequencyDict = makeFrequencyDict(filename, minSetSize)
	
	#iterate over dictionary, write entries that occur >= sigma times
	for key, value in frequencyDict.items():
		if value >= sigma:
			string = ''
			string += str(len(key)) + ', ' + str(value) #set size, frequency
			for item in key:
				string += ', ' + str(item) #each item id
			string += '\n'
			outfile.write(string)









