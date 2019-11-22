'''
https://github.com/bkrawciw-mines/Week12-utility.git
Benjamin Krawciw
CSCI 102 Section A
Week 12
'''

#Print output
def PrintOutput(string):
    string = str(string)
    print('OUTPUT '+string)
    
#Load file
def LoadFile(path):
    outList = []
    with open(path) as file:
        for line in file:
            outList.append(line.rstrip())
    return outList

#Load file test
'''
lines = LoadFile('test.txt')
PrintOutput(lines)
'''

#Update string
def UpdateString(main_string, mod_string, i):
    newString = main_string[0:i]+mod_string+main_string[i+1:]
    PrintOutput(newString)

#UpdateString test
'''
UpdateString("Hello world", 'a', 3)
'''