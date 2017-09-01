'''
Created on Aug 31, 2017

@author: jlearx
'''

def PrintDict(dictionary):
    for pair in dictionary.items():
        print(pair)

def CountItem(dictionary, item):
    if (item in dictionary):
        count = dictionary[item] + 1
        dictionary[item] = count
    else:
        dictionary[item] = 1

if __name__ == '__main__':
    nameFile = "../nameslist.txt"
    sundbFile = "../Training_01.txt"
    nameDict = {}
    sundbDict = {}
    
    # Read and parse the name file
    with open(nameFile, 'r') as open_file:
        line = open_file.readline()
        
        while line:
            line = line.rstrip('\n')
            CountItem(nameDict, line)
            line = open_file.readline()
    
    PrintDict(nameDict)
    
    # Read and parse the sundb file
    with open(sundbFile, 'r') as open_file:
        line = open_file.readline()
        
        while line:
            line = line.rstrip('\n')
            category = line.split('/')[2]
            CountItem(sundbDict, category)
            line = open_file.readline()
    
    PrintDict(sundbDict)
    
    
    
