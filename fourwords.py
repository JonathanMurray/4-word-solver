import codecs

def isFullOfSome(longWord, shortWords):
    foundFirstMatch = False
    foundSecondMatch = False
    for shortWord in shortWords:
        if shortWord == longWord[1:]:
            foundFirstMatch = True
        if shortWord == longWord[:len(longWord)-1]:
            foundSecondMatch = True
        if foundFirstMatch and foundSecondMatch:
            return True
    return False

def getFilteredWords(fileName):
    f = codecs.open(fileName, 'r', "ISO-8859-1")
    length4 = []
    length3 = []
    length2 = []
    print "loading words..."
    for word in f:
        word = word.strip()
        if len(word) == 4:
            length4.append(word)
        if len(word) == 3:
            length3.append(word)
        if len(word) == 2:
            length2.append(word)
    print "total # of 3words: " + str(len(length3))
    print "removing some 3words..."    
    copyOfLength3 = list(length3)
    for word3 in copyOfLength3:
        if not isFullOfSome(word3, length2):
            length3.remove(word3)
    print "total # of 4words: " + str(len(length4))
    print "removing some 4words..."
    copyOfLength4 = list(length4)
    for word4 in copyOfLength4:
        if not isFullOfSome(word4, length3):
            length4.remove(word4)
    return [length4, length3, length2]



def getPerfectBoard(board):
    bestBoard = None
    bestScore = 0
    for (wordIndex, w0) in enumerate(length4):
        print str(wordIndex) + " out of " + str(len(length4))
        board[0] = w0
        for w1 in length4:
            
            board[1] = w1
            for w2 in length4:
                
                board[2] = w2
                for w3 in length4:
                    board[3] = w3
                    score = getScore(board, False)
                    if score >= bestScore:
                        bestScore = score
                        getScore(board, True)
                        bestBoard = list(board)
                        print board
                        print "SCORE: " + str(score)
                    #if getScore(board) == OPTIMAL_SCORE:
                    #    return board          

def getScore(board, printScore):
    score = 0
    for row in board:
        rowScore = getRowScore(row)
        if printScore:
            print row + " gets " + str(rowScore)
        score += rowScore
    columns = ["","","",""]
    for i in range(4):
        columns[i] = ""
        for j in range(4):
            columns[i] += board[j][i]
    for column in columns:
        colScore = getRowScore(column)
        score += colScore
        if printScore:
            print column + " gets " + str(colScore)
    return score
        
def getRowScore(row):
    score = 0
    if row in length4:
        score += 5
    if row[1:] in length3:
        score += 3
    if row[:3] in length3:
        score += 3
    if row[2:] in length2:
        score += 2
    if row[1:3] in length2:
        score += 2
    if row[:2] in length2:
        score += 2
    return score               

OPTIMAL_SCORE = 136




words = getFilteredWords("swedish-word-list")
print "words loaded."
length4 = words[0]
length3 = words[1]
length2 = words[2]

print str(len(length4)) + " relevant length4-words"
print str(len(length3)) + " relevant length3-words"
print str(len(length2)) + " relevant length2-words"

board = ["","","",""] #The strings represent rows in the board

#print length4

board = getPerfectBoard(board)
                        


    
