'''
Created on Aug 31, 2017

@author: jlearx
'''

def PrintDict(dictionary):
    for pair in dictionary.items():
        print(pair)

def ProcessNameLine(nameDict, line):
    
    if (line in nameDict):
        count = nameDict[line]
        nameDict[line] = ++count
    else:
        nameDict[line] = 1

if __name__ == '__main__':
    nameFile = "../nameslist.txt"
    nameDict = {}
    
    with open(nameFile, 'r') as open_file:
        line = open_file.readline()
        
        while line:
            ProcessNameLine(nameDict, line)
            line = open_file.readline()
    
    PrintDict(nameDict)
