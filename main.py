import kivy
kivy.require('1.9.2')

from kivy.config import Config
Config.set('modules', 'screen', 'ipad,portrait')
from random import randint
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, ObjectProperty, BooleanProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import *
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.label import Label

#EDIT
#Add a ListProperty for Hero names in NewGame
#Add StringProperty for Hero in Player
#To use Hero ability just put where you think the ability should be for now and check if 
#Player.hero == <HeroName>
#or
#Add a Hero class?
#idk how to implement yet

class Builder(Widget):
	type=StringProperty('')
	player=ObjectProperty()
	num=NumericProperty(0)
	tile=ObjectProperty(None)
	isSelected=BooleanProperty(False)
	
	#EDIT
	#Methods you can add
	#
	#isAdjacentToFriendlyTerritory
	#isAdjacentToEnemyTerritory
	#isBorderingFriendlyTerritory
	#isBorderingEnemyTerritory
	#Use GridTile.flag, player should be equal to flag-1 to be of friendly territory
	#
	#isAdjacentToFriendlyBuilder
	#isAdjacentToEnemyBuilder
	#isBorderingFriendlyBuilder
	#isBorderingEnemyBuilder
	#isBordering
	
	def isAdjacentToFriendlyTerritory(self):
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).owner is not None:
					if self.tile.getGrid().getTile(x + i, y + j).owner.num == self.player.num:
						return True
		return False
		
	def isAdjacentToEnemyTerritory(self):
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).owner is not None:
					if self.tile.getGrid().getTile(x + i, y + j).owner.num != self.player.num:
						return True
		return False
	
	def isBorderingFriendlyTerritory(self):
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if i != 0 and j != 0:
					pass
				elif x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).owner is not None:
					if self.tile.getGrid().getTile(x + i, y + j).owner.num == self.player.num:
						return True
		return False
		
	def isBorderingEnemyTerritory(self):
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if i != 0 and j != 0:
					pass
				elif x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).owner is not None:
					if self.tile.getGrid().getTile(x + i, y + j).owner.num != self.player.num:
						return True
		return False
		
	def isAdjacentToFriendlyBuilder(self):
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).isOccupied():
					if self.tile.getGrid().getTile(x + i, y + j).getOccupier().player.num == self.player.num:
						return True
		return False
		
	def isAdjacentToEnemyBuilder(self):
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).isOccupied():
					if self.tile.getGrid().getTile(x + i, y + j).getOccupier().player.num != self.player.num:
						return True
		return False
		
	def isBorderingFriendlyBuilder(self):
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if i != 0 and j != 0:
					pass
				elif x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).isOccupied():
					if self.tile.getGrid().getTile(x + i, y + j).getOccupier().player.num == self.player.num:
						return True
		return False
		
	def isBorderingEnemyBuilder(self):
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if i != 0 and j != 0:
					pass
				elif x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).isOccupied():
					if self.tile.getGrid().getTile(x + i, y + j).getOccupier().player.num != self.player.num:
						return True
		return False
		
		
	
	def canMoveTo(self, xInt, yInt):
		'''
		Checks whether this builder can move to the tile on the grid with
		specified x and y coordinates.
		'''
		#Things to check
		#First, make sure that it's actually adjacent and within bounds
		#Next, check whether the tile being moved to is occupied and/or is domed
		#Finally, check whether the height lets you move
		range = 1
		valid = True
		
		if self.player.opponent.hero == 'Bacchus':
			if self.isAdjacentToEnemyBuilder():
				if self.tile.getX() == xInt or self.tile.getY() == yInt:
					valid = False
		
		if self.player.hero == 'Mercury':
			if self.isAdjacentToFriendlyTerritory():
				range += 1
		
		if valid:
			if xInt == -1 or yInt == -1 or xInt == 5 or yInt == 5:
				valid = False
			if self.tile.getX() > xInt+range or self.tile.getX() < xInt-range:
				valid = False
			if self.tile.getY() > yInt+range or self.tile.getY() < yInt-range:
				valid = False
			if self.tile.getX() == xInt and self.tile.getY() == yInt:
				valid = False
			if valid:
				if self.tile.getGrid().getTile(xInt,yInt).isDomed() or self.tile.getGrid().getTile(xInt,yInt).isOccupied():
					valid = False
				if valid:
					if self.tile.getGrid().getTile(xInt,yInt).getLevel() - self.tile.getLevel() > 1:
							valid = False
		return valid
		
	def canBuildOn(self, xInt, yInt):
		'''
		Checks whether this builder can build on the tile on the grid with
		specified x and y coordinates.
		'''
		#Things to check
		#First, make sure that it's actually adjacent and within bounds
		#Next, check whether the tile being moved to is occupied and/or is domed
		#Lastly, check if we actually have a piece available
		range = 1
		valid = True
		if valid:
			if xInt == -1 or yInt == -1 or xInt == 5 or yInt == 5:
				valid = False
			if self.tile.getX() > xInt+range or self.tile.getX() < xInt-range:
				valid = False
			if self.tile.getY() > yInt+range or self.tile.getY() < yInt-range:
				valid = False
			if self.tile.getX() == xInt and self.tile.getY() == yInt:
				valid = False
			if valid:
				target = self.tile.getGrid().getTile(xInt,yInt)
				if target.isDomed() or target.isOccupied():
					valid = False
				if valid:
					if self.tile.getGrid().getUsed(target.getLevel()) == self.tile.getGrid().getCap(target.getLevel()):
						valid = False
		return valid
	
	def moveBuilder(self, xInt, yInt, x, y):
		if self.canMoveTo(xInt, yInt):
			self.pos = x, y
			return True
		return False
	
	def setTile(self, tile):
		self.tile = tile
	
	def getTile(self):
		return self.tile
		
	def getPlayer(self):
		return self.player
		
	def getNum(self):
		return self.num

class GridTile(Widget):
	level = NumericProperty(0)
	domed = BooleanProperty(False)
	xInt = NumericProperty(0)
	yInt = NumericProperty(0)
	position = ReferenceListProperty(xInt, yInt)
	grid = ObjectProperty(None)
	occupied = BooleanProperty(False)
	occupier = ObjectProperty(None, allownone=True)
	source0 = StringProperty('')
	source1 = StringProperty('')
	source2 = StringProperty('')
	source3 = StringProperty('')
	source4 = StringProperty('')
	sources = ReferenceListProperty(source0, source1, source2, source3, source4)
	flag = NumericProperty(0) #0-Neutral, 1-player0, 2-player1
	flag0 = StringProperty('')
	flag1 = StringProperty('')
	flag2 = StringProperty('')
	flags = ReferenceListProperty(flag0, flag1, flag2)
	owner = ObjectProperty(None, allownone = True)
	
	def build(self):
		if self.level < 3:
			self.level += 1
			self.grid.tileUsed(self.level)
		elif self.domed is False:
			#self.level = 4
			self.grid.tileUsed(self.level)
			self.domed = True
		else:
			raise Exception
			
	def getLevel(self):
		return self.level
		
	def getOccupier(self):
		return self.occupier
		
	def isDomed(self):
		return self.domed
		
	def isOccupied(self):
		return self.occupied
	
	def setGrid(self, grid):
		self.grid = grid
	
	def getGrid(self):
		return self.grid
		
	def getX(self):
		return self.position[0]
	
	def getY(self):
		return self.position[1]
		
	def occupy(self, builder):
		self.occupied = True
		self.occupier = builder
		self.occupier.setTile(self)
		
	def unoccupy(self):
		self.occupied = False
		self.occupier = None
		
class Grid(Widget):
	
	tileHold = ObjectProperty(None)
	tile11=ObjectProperty(None)
	tile12=ObjectProperty(None)
	tile13=ObjectProperty(None)
	tile14=ObjectProperty(None)
	tile15=ObjectProperty(None)
	tile21=ObjectProperty(None)
	tile22=ObjectProperty(None)
	tile23=ObjectProperty(None)
	tile24=ObjectProperty(None)
	tile25=ObjectProperty(None)
	tile31=ObjectProperty(None)
	tile32=ObjectProperty(None)
	tile33=ObjectProperty(None)
	tile34=ObjectProperty(None)
	tile35=ObjectProperty(None)
	tile41=ObjectProperty(None)
	tile42=ObjectProperty(None)
	tile43=ObjectProperty(None)
	tile44=ObjectProperty(None)
	tile45=ObjectProperty(None)
	tile51=ObjectProperty(None)
	tile52=ObjectProperty(None)
	tile53=ObjectProperty(None)
	tile54=ObjectProperty(None)
	tile55=ObjectProperty(None)
	y1=ReferenceListProperty(tile11, tile21, tile31, tile41, tile51)
	y2=ReferenceListProperty(tile12,tile22,tile32,tile42,tile52)
	y3=ReferenceListProperty(tile13, tile23, tile33, tile43, tile53)
	y4=ReferenceListProperty(tile14,tile24,tile34,tile44,tile54)
	y5=ReferenceListProperty(tile15, tile25, tile35, tile45, tile55)
	matrix = ReferenceListProperty(y1,y2,y3,y4,y5)
	levelUsed = ListProperty([0,0,0,0])
	levelCap = ListProperty([16,14,12,14])
	
	def setTileGrid(self):
		for y in self.matrix:
			for x in y:
				x.setGrid(self)

	def setMatrix(self, matrix):
		self.matrix = matrix
	
	def getTile(self, x, y):
		return self.matrix[x][y]
		
	def getUsed(self, level):
		return self.levelUsed[level]
	
	def getCap(self, level):
		return self.levelCap[level]
		
	def tileUsed(self, level):
		self.levelUsed[level - 1] += 1
	
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
class Player(Widget):
	grid = ObjectProperty(None)
	num = NumericProperty(0)
	builder0 = ObjectProperty(None)
	builder1 = ObjectProperty(None)
	builder = ReferenceListProperty(builder0, builder1)
	hero = StringProperty('')
	opponent = ObjectProperty
	
	def move(self):
		pass
		
	def build(self):
		pass
		
	def checkWin(self):
		return self.builder[0].getTile().getLevel() == 3 or self.builder[1].getTile().getLevel() == 3
		pass
		
	def checkLose(self):
		canMove = False
		x = []
		y = []
		for i in self.builder:
			x.append(i.getTile().getX())
			y.append(i.getTile().getY())
		
		for i in range(5):
			for j in range(5):
				for k in (0,1):
					canMove=canMove or self.builder[k].canMoveTo(i,j)
				if canMove is True:
					break
			if canMove is True:
				break
				
		return (not canMove)
		#return True

class NewGame(Widget):
	text = StringProperty('')
	player0 = ObjectProperty(None)
	player1 = ObjectProperty(None)
	players = ReferenceListProperty(player0, player1)
	grid = ObjectProperty(None)
	gPhase = 0
	current = NumericProperty(0) #Builder selected
	player = 0 #Current Player (0, 1) 0 is named Player1, 1 is Player2
	xP=NumericProperty(0)
	yP=NumericProperty(0)
	xB =NumericProperty(0)
	yB =NumericProperty(0)
	builder00=ObjectProperty(None)
	builder01=ObjectProperty(None)
	builder10=ObjectProperty(None)
	builder11=ObjectProperty(None)
	builder = ReferenceListProperty(builder00, builder01, builder10, builder11)
	heroes = ListProperty(['Bacchus','Mercury'])
	
	def init(self):
		self.grid.setTileGrid()
	
	def update(self,dt):
		pass
	
	def on_touch_up(self, touch):
		if touch.x < self.width/5:
			self.xP=0
		elif touch.x < self.width*2/5:
			self.xP=1
		elif touch.x < self.width*3/5:
			self.xP=2
		elif touch.x < self.width*4/5:
			self.xP=3
		elif touch.x < self.width*5/5:
			self.xP=4
		if touch.y < self.grid.getY():
			self.yP = 5
		elif touch.y < self.grid.width/5 + self.grid.getY():
			self.yP=0
		elif touch.y < self.grid.width*2/5 + self.grid.getY():
			self.yP=1
		elif touch.y < self.grid.width*3/5 + self.grid.getY():
			self.yP=2
		elif touch.y < self.grid.width*4/5 + self.grid.getY():
			self.yP=3
		elif touch.y < self.grid.width*5/5 + self.grid.getY():
			self.yP=4
		else:
			self.yP=5
		
		if self.yP == 5:
			pass
		
		#Initial Phase
		elif self.gPhase == 0:
			if not self.grid.getTile(self.xP, self.yP).isOccupied():
				self.grid.getTile(self.xP, self.yP).occupy(self.builder[self.current])
				self.builder[self.current].setTile(self.grid.getTile(self.xP, self.yP))
				self.builder[self.current].pos = self.grid.width/5*self.xP, self.grid.width/5*self.yP + self.grid.getY()
				self.current += 1
				if self.current == 4:
					self.current = 0
					self.gPhase = 1
				
		#Choose  Phase
		elif self.gPhase == 1:
			if self.grid.getTile(self.xP, self.yP).isOccupied():
				if self.grid.getTile(self.xP, self.yP).getOccupier().getPlayer().num == self.player:
					self.grid.getTile(self.xP,self.yP).getOccupier().isSelected = True
					self.current = self.grid.getTile(self.xP, self.yP).getOccupier().getNum()
					self.xB = self.xP
					self.yB = self.yP
					self.gPhase = 2
			pass
		
		#Move Phase
		elif self.gPhase == 2:
			#Checks if selected tile contains the selected Builder
			if self.builder[self.current].getTile().getX()==self.xP and self.builder[self.current].getTile().getY()==self.yP:
				self.grid.getTile(self.xP,self.yP).getOccupier().isSelected = False
				self.gPhase = 1
			#Checks if the selected tile contains a Builder owned by the current Player
			elif self.grid.getTile(self.xP, self.yP).isOccupied():
				if self.grid.getTile(self.xP, self.yP).getOccupier().getPlayer().num == self.player:
					self.grid.getTile(self.xB,self.yB).getOccupier().isSelected = False
					self.grid.getTile(self.xP,self.yP).getOccupier().isSelected = True
					self.current = self.grid.getTile(self.xP, self.yP).getOccupier().getNum()
					self.xB = self.xP
					self.yB = self.yP
			#Checks if the selected Builder can move to the selected tile
			elif self.builder[self.current].moveBuilder(self.xP, self.yP, self.grid.width/5*self.xP, self.grid.width/5*self.yP + self.grid.getY()):
				self.grid.getTile(self.xB, self.yB).unoccupy()
				self.grid.getTile(self.xP, self.yP).occupy(self.builder[self.current])
				self.xB = self.xP
				self.yB = self.yP
				self.gPhase = 3
				#Checks if the current Player won by moving
				if self.players[self.player].checkWin():
					self.text = 'PLAYER '+str(self.player + 1)+' WINS!'
					self.gPhase = 4
			
		#Build Phase
		elif self.gPhase ==3:
			#Checks if the selected Builder can build on the selected GridTile
			if self.builder[self.current].canBuildOn(self.xP, self.yP):
				
				self.grid.getTile(self.xB,self.yB).getOccupier().isSelected = False
				self.grid.getTile(self.xP, self.yP).build()
				#Adds or Removes a flag on the selected GridTile
				if self.grid.getTile(self.xP, self.yP).isDomed():
					self.grid.getTile(self.xP, self.yP).flag = 0
					self.grid.getTile(self.xP, self.yP).owner = None
				else:
					self.grid.getTile(self.xP, self.yP).flag = self.player + 1
					self.grid.getTile(self.xP, self.yP).owner = self.players[self.player]
			if True:
				self.gPhase = 1
				self.player = (self.player + 1) % 2
				#Checks if any Player lost by being disabled
				for i in (0,1):
					if self.players[i].checkLose():
						self.text = 'PLAYER '+str((i + 1)%2 +1)+' WINS!'
						self.gPhase =4
				pass
				
		elif self.gPhase == 4:
			pass

class NewApp(App):

    def build(self):
    	game = NewGame()
    	game.init()
    	#game.init()
    	#game.initGame()
    	#Clock.schedule_interval(game.update, 1.0 / 60.0)
    	return game
    	
    def on_pause(self):
    	return True


if __name__ in ('__main__','__android__'):
    NewApp().run()