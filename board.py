class Cell:
	def __init__(self,letter,letterBonus,wordBonus):
		self.letter=letter
		self.letterBonus=letterBonus
		self.wordBonus=wordBonus
		
class Tile:
	def __init__(self,letter,score,count):
		self.letter=letter
		self.score=score
		self.count=count
		
	def countGreaterThanZero(self):
		if self.count>0:
			return True
		else:
			return False
	
	def decrementCount(self):
		self.count-=1
		
class Board:
	#dir is 0 for right and 1 for down
	#(0,0) is the top left corner of the board
	def __init__(self):
		self.board=[[Cell('-',1,1) for i in range(15)] for j in range(15)]
		self.addBonuses()
		self.initTiles()
	
	def initTiles(self):
		self.Tiles={'a':Tile('a',1,9),	'b':Tile('b',3,2), 
					'c':Tile('c',3,2),	'd':Tile('d',2,4), 
					'e':Tile('e',1,12),	'f':Tile('f',4,2),
					'g':Tile('g',2,3),	'h':Tile('h',4,2), 
					'i':Tile('i',1,9),	'j':Tile('j',8,1), 
					'k':Tile('k',5,1),	'l':Tile('l',1,4),
					'm':Tile('m',3,2),	'n':Tile('n',1,6), 
					'o':Tile('o',1,8), 	'p':Tile('p',3,2), 'q':Tile('q',10,1),	'r':Tile('r',1,6),
					's':Tile('s',1,4),	't':Tile('t',1,6), 'u':Tile('u',1,4),	'v':Tile('v',4,2), 'w':Tile('w',4,2),	'x':Tile('x',8,1),
					'y':Tile('y',4,2),	'z':Tile('z',10,1), '-':Tile('-',0,2)}

	def addBonuses(self):
		#key of dictionary bonuses: (letterBonus,wordBonus)
		#(2,1)=> double letter score
		bonuses={(2,1):[[0,3],[2,6],[3,0],[3,7],[6,2],[6,6],[7,3]],
		(1,2):[[1,1],[2,2],[3,3],[4,4]],
		(3,1):[[1,5],[5,1],[5,5]],
		(1,3):[[0,0],[0,7],[7,0]]
		}
		for type in bonuses.keys():
			for j in bonuses[type]:
				obj=self.board[j[0]][j[1]]
				obj.letterBonus=type[0]
				obj.wordBonus=type[1]
				
	def computeScore(self,word, row, col, dir):#board, row no, col no, dir
		sum = 0
		bonusScore = 1
		for i in word:
			sum = sum + self.Tiles[i].score * self.board[row][col].letterBonus
			bonusScore = bonusScore * self.board[row][col].wordBonus
			row = row + dir
			col = col + (1 - dir)			
		sum = sum * bonusScore
		return sum


board1 = Board()
print(board1.computeScore("mentally",1,6,0))
