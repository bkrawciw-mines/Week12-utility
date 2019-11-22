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

#Find word count
def FindWordCount(listy, string):
    count = 0
    for item in listy:
        count += item.count(string)
    return count

#FindWordCount test
'''
lines = LoadFile('test.txt')
PrintOutput(FindWordCount(lines, 'h'))
'''

#Score Finder
def ScoreFinder(players, scores, player):
    #Makes names lowercase
    for i in range(len(players)):
        players[i] = players[i].lower()
    l_player = player.lower()
    
    #Finding player
    index = None
    for i in range(len(players)):
        if players[i] == l_player:
            index = i
    if index == None:
        PrintOutput('player not found')
    else:
        PrintOutput(player.capitalize()+' got a score of '+str(scores[index]))

#ScoreFinder test
'''
players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
scores = [5, 8, 10, 6, 10, 4]
ScoreFinder(players, scores, "jill")
ScoreFinder(players, scores, "Manuel")
'''

#Union
def Union(listA, listB):
    listC = []
    for item in listA:
        if item not in listC:
            listC.append(item)
    for item in listB:
        if item not in listC:
            listC.append(item)
    return(listC)

#Union test
'''
players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
scores = [5, 8, 10, 6, 10, 4]
PrintOutput(Union(scores, players2))
'''