from copy import deepcopy

#dir is 0 for right and 1 for down
#(0,0) is the top left corner of the board
def initLetterScores():
    letterScores = {"-":0,"aeioulnrst":1,"dg":2,"bcmp":3,"fhvwy":4,"k":1,"jx":8,"qz":10}
    return letterScores

def initBoard(bonus):
    board = []
    initList = ["0",1,1]#letter,letterbonus,wordbonus
    lst = []
    print deepcopy(initList)
    a = deepcopy(initList)
    for i in range(15):
        lst.append(deepcopy(initList))
    for i in range(15):
        board.append(deepcopy(lst))

    for j in range(4):
        for i in bonus[j]:
            type = j//2 + 1
            val = j % 2 + 2
            board[i[0]][i[1]][type],board[14 - i[0]][i[1]][type],board[i[0]][14 - i[1]][type],board[14 - i[0]][14 - i[1]][type] = [val]*4
    return board

def initBonus():
    dls = [[0,3],[2,6],[3,0],[3,7],[6,2],[6,6],[7,3]]
    dws = [[1,1],[2,2],[3,3],[4,4]]
    tls = [[1,5],[5,1],[5,5]]
    tws = [[0,0],[0,7],[7,0]]
    b = [dls,dws,tls,tws]
    bonus = [dls[:],dws[:],tls[:],tws[:]]
    return bonus

def computeScore(word, row, col, dir,board,letterScores):
    sum = 0
    bonusScore = 1
    for i in word:
        for j in letterScores.keys():
           if i in j:
                sum = sum + letterScores[j] * board[row][col][1]
                bonusScore = bonusScore * board[row][col][2]
        row = row + dir
        col = col + (1 - dir)
        print sum
        
    sum = sum * bonusScore
    return sum


board = initBoard(initBonus())
letterScores = initLetterScores()
print(computeScore("idiot",1,6,0,board,letterScores))
