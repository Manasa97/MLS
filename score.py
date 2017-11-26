#dir is 0 for right and 1 for down
#(0,0) is the top left corner of the board
def initLetterScores():
    letterScores = {"-":0,"aeioulnrst":1,"dg":2,"bcmp":3,"fhvwy":4,"k":1,"jx":8,"qz":10}
    return letterScores

def initBoard():
    board = []
    initDict = {"letter":"0","letterBonus":1,"wordBonus":1}
    list = []
    for j in range(15):
        list.append(initDict)
    for i in range(15):
        board.append(list)
    return board
    #*15 doesn't work

def computeScore(word, row, col, dir,board,letterScores):#board, row no, col no, dir
    sum = 0
    bonusScore = 1
    for i in word:
        for j in letterScores.keys():
           if i in j:
                sum = sum + letterScores[j] * board[row][col]["letterBonus"]
                bonusScore = bonusScore * board[row][col]["wordBonus"]
        row = row + dir
        col = col + (1 - dir)
        
    sum = sum * bonusScore
    return sum


board = initBoard()
letterScores = initLetterScores()
print(computeScore("mentally",1,6,0,board,letterScores))
