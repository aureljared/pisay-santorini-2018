import kivy
kivy.require('1.9.2')

from kivy.config import Config
Config.read('config.ini')
#Config.set('modules','screen','onex, portrait')
Config.write()
from random import randint
from random import sample
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, ObjectProperty, BooleanProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import *
from kivy.core.window import Window
#from kivy.core.sound import SoundLoader

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
	tile=ObjectProperty(None, allownone = True)
	isSelected=BooleanProperty(False)
	isActive=BooleanProperty(True)
	tileSave=ObjectProperty(None, allownone = True)
	
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
		'''
		Returns true if a builder is adjacent, in the four cardinal directions or in the four diagonal directions, to friendly territory.
		A territory is described as friendly if it was last built on by a builder owned by this player.
		'''
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					continue
				elif self.tile.getGrid().getTile(x + i, y + j).owner is not None:
					if self.tile.getGrid().getTile(x + i, y + j).owner.num == self.player.num:
						return True
		return False
		
	def isAdjacentToEnemyTerritory(self):
		'''
		Returns true if a builder is adjacent, in the four cardinal directions or in the four diagonal directions, to enemy territory.
		A territory is described as enemy if it was last built on by a builder owned by another player.
		'''
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
		'''
		Returns true if a builder is bordering, in the four cardinal directions, friendly territory.
		A territory is described as friendly if it was last built on by a builder owned by this player.
		'''
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
		'''
		Returns true if a builder is bordering, in the four cardinal directions, enemy territory.
		A territory is descibed as enemy if it was last built on by a builder owned by another player.
		'''
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
		'''
		Returns true if a builder is adjacent, in the four cardinal directions or in the four diagonal directions, to a friendly builder.
		'''
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5 or i == 0 and j == 0:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).isOccupied():
					if self.tile.getGrid().getTile(x + i, y + j).getOccupier().player.num == self.player.num:
						return True
		return False
		
	def isAdjacentToEnemyBuilder(self):
		'''
		Returns true if a builder is adjacent, in the four cardinal directions or in the four diagonal directions, to an enemy builder.
		'''
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5 or i == 0 and j == 0:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).isOccupied():
					if self.tile.getGrid().getTile(x + i, y + j).getOccupier().player.num != self.player.num:
						return True
		return False
		
	def isBorderingFriendlyBuilder(self):
		'''
		Returns true if a builder is bordering, in the four cardinal directions, a friendly builder.
		'''
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if i != 0 and j != 0:
					pass
				elif x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5 or i == 0 and j == 0:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).isOccupied():
					if self.tile.getGrid().getTile(x + i, y + j).getOccupier().player.num == self.player.num:
						return True
		return False
		
	def isBorderingEnemyBuilder(self, count):
		'''
		Returns true if a builder is bordering, in the four cardinal directions, an enemy builder.
		'''
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		n = 0
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if i != 0 and j != 0:
					pass
				elif x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5 or i == 0 and j == 0:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).isOccupied():
					if self.tile.getGrid().getTile(x + i, y + j).getOccupier().player.num != self.player.num:
						n += 1
					if n == count:
						return True
		return False
	
	def die(self):
		'''
		Removes this builder from the game.
		'''
		self.tile.unoccupy()
		self.tile = None
		self.isActive = False
	
	##
	
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
		
		#Bacchus
		#Checks wether your Builder is adjacent to a Builder owned by an enemy Bacchus
		#If Yes, your Builder can't move vertically or horizontally
		if self.player.opponent.hero == 'Bacchus':
			if self.isBorderingEnemyBuilder():
				if self.tile.getX() == xInt or self.tile.getY() == yInt:
					valid = False
		##
		
		#Mercury
		#Checks wether your Builder is adjacent to a GridTile with your Flag
		#If Yes, range is increased by 1
		if self.player.hero == 'Mercury':
			if self.isAdjacentToFriendlyTerritory():
				range += 1
		##
		
		if valid:
			if xInt == -1 or yInt == -1 or xInt == 5 or yInt == 5:
				valid = False
			if self.tile.getX() > xInt+range or self.tile.getX() < xInt-range:
				valid = False
			if self.tile.getY() > yInt+range or self.tile.getY() < yInt-range:
				valid = False
			if self.tile.getX() == xInt and self.tile.getY() == yInt:
				valid = False
			
			#Janus
			#If selected GridTile is bordering your Builder, allow move
			if self.player.hero == 'Janus':
				if self.tile.getGrid().getTile(xInt,yInt).isBorderingBuilder(self.player.num):
					valid = True
			##
					
			if valid:
				if self.tile.getGrid().getTile(xInt,yInt).isDomed():
					valid = False
				if self.tile.getGrid().getTile(xInt,yInt).isOccupied():
					
					#Apollo
					#If selected GridTile is occupied by an enemy Builder, allow move
					if self.player.hero == 'Apollo' and self.tile.getGrid().getTile(xInt,yInt).getOccupier().player.num != self.player.num:
						pass
					##
						
					else:
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
	
	def moveBuilder(self, xInt, yInt):
		'''
		Moves this builder to a tile with the specified x and y coordinates.
		'''
		if self.canMoveTo(xInt, yInt):
			
			#Apollo
			#Swap places with the Builder occupying selected GridTile
			if self.player.hero == 'Apollo' and self.tile.grid.getTile(xInt, yInt).isOccupied():
				builder = self.tile.grid.getTile(xInt, yInt).getOccupier()
				builder.tile.unoccupy()
				self.tile.occupy(builder)
			##
				
			else:
				self.tile.unoccupy()
			self.tile.grid.getTile(xInt, yInt).occupy(self)
			return True
		return False
	
	def setTile(self, tile):
		'''
		Sets the tile that the builder is on.
		'''
		self.tile = tile
	
	def getTile(self):
		'''
		Gets the tile that the builder is on.
		'''
		return self.tile
		
	def getPlayer(self):
		'''
		Gets the player that owns the builder.
		'''
		return self.player
		
	def getNum(self):
		'''
		Gets the number assigned to this builder for identification.
		'''
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
	flag3 = StringProperty('')
	flag4 = StringProperty('')
	flags = ReferenceListProperty(flag0, flag1, flag2, flag3, flag4)
	owner = ObjectProperty(None, allownone = True)
	levelSave = NumericProperty(0)
	domedSave = BooleanProperty(False)
	flagSave = NumericProperty(0)
	ownerSave = ObjectProperty(None, allownone = True)
	
	#EDIT
	#May need check methods similar to those in Builder
	
	def isBorderingBuilder(self, num):
		'''
		Returns true if a builder is bordering, in the four cardinal directions, a builder.
		'''
		x = int(self.getX())
		y = int(self.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if i != 0 and j != 0:
					pass
				elif x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5 or i == 0 and j == 0:
					pass
				elif self.getGrid().getTile(x + i, y + j).isOccupied():
					if self.getGrid().getTile(x + i, y + j).getOccupier().player.num == num:
						return True
		return False
		
	def isAdjacentToBuilder(self, num):
		'''
		Returns true if a builder is adjacent, in the four cardinal directions or in the four diagonal directions, to a builder.
		'''
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.getGrid().getTile(x + i, y + j).isOccupied():
					if self.getGrid().getTile(x + i, y + j).getOccupier().player.num == num:
						return True
		return False
		
	##
	def unflag(self):
		self.flag = 0
		self.owner = None
	
	def build(self):
		'''
		Increases the level of the building on this tile if it is not at level 3, and builds a dome otherwise.
		'''
		if self.level < 3:
			self.level += 1
			self.grid.tileUsed(self.level)
		elif self.domed is False:
			self.dome()
		else:
			raise Exception
			
	def dome(self):
		'''
		Adds a dome to this grid tile.
		'''
		self.grid.tileUsed(4)
		self.domed = True
			
	def getLevel(self):
		'''
		Gets the level of the building on this tile.
		'''
		return self.level
		
	def getOccupier(self):
		'''
		Gets which builder occupies this tile.
		'''
		#Verify the documentation
		return self.occupier
		
	def isDomed(self):
		'''
		Returns true if this grid tile has a dome.
		'''
		return self.domed
		
	def isOccupied(self):
		'''
		Checks if this tile is occupied by a builder.
		'''
		return self.occupied
	
	def setGrid(self, grid):
		'''
		Sets the grid on which this tile is on.
		'''
		self.grid = grid
	
	def getGrid(self):
		'''
		Gets the grid on which this tile is on.
		'''
		return self.grid
		
	def getX(self):
		'''
		Gets the x-cooridinate of this tile.
		'''
		return self.position[0]
	
	def getY(self):
		'''
		Gets the y-cooridinate of this tile.
		'''
		return self.position[1]
		
	def occupy(self, builder):
		'''
		Changes the status of the tile as being occupied by a given builder.
		'''
		self.occupied = True
		self.occupier = builder
		self.occupier.setTile(self)
		builder.pos = self.pos
		
	def unoccupy(self):
		'''
		Changes the status of the tile as no longer being occupied by a given builder.
		'''
		self.occupied = False
		self.occupier = None
		
class Grid(Widget):
	'''
	A representation of the 5 by 5 grid used in the game.
	'''
	
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
	timer = ListProperty([0,0,0,0,0,0])
	
	def setTileGrid(self):
		'''
		Sets the tile grid.
		'''
		for y in self.matrix:
			for x in y:
				x.setGrid(self)

	def setMatrix(self, matrix):
		'''
		Sets the matrix of the tile grid.
		'''
		self.matrix = matrix
	
	def getTile(self, x, y):
		'''
		Gets the tile with the specified x and y coordinates in that order.
		'''
		return self.matrix[x][y]
		
	def getUsed(self, level):
		'''
		Gets the current number of used tiles of a given building level.
		'''
		return self.levelUsed[level]
		
	def getUnused(self, level):
		'''
		Gets the current number of unused tiles of a given building level.
		'''
		return self.levelCap[level] - self.levelUsed[level]
	
	def getCap(self, level):
		'''
		Gets the maximum number of tiles of a given building level.
		'''
		return self.levelCap[level]
		
	def tileUsed(self, level):
		'''
		Uses a tile of a given building level.
		'''
		self.levelUsed[level - 1] += 1
	
	def getX(self):
		'''
		Gets the x-coordinate of the graphical representation of the widget of the grid.
		'''
		return self.x
		
	def getY(self):
		'''
		Gets the y-coordinate of the graphical representation of the widget of the grid.
		'''
		return self.y
		
class Player(Widget):
	'''
	A representation of the players interacting with the game.
	'''
	color = ListProperty([0,0,0])
	grid = ObjectProperty(None)
	num = NumericProperty(0)
	type = StringProperty('')
	isActive = BooleanProperty(False)
	builder0 = ObjectProperty(None)
	builder1 = ObjectProperty(None)
	
	#Extra Builders
	builder2 = ObjectProperty(None)
	builder3 = ObjectProperty(None)
	##
	
	builder = ReferenceListProperty(builder0, builder1, builder2, builder3)
	hero = StringProperty('')
	opponent = ObjectProperty(None)
	isCurrent = BooleanProperty(False)
	skillActive = BooleanProperty(False)
	activatedSkill = NumericProperty(0)
	maxActive = NumericProperty(1)
	
	def move(self):
		'''
		Depreciated. Do not use.
		'''
		pass
		
	def build(self):
		'''
		Depreciated. Do not use.
		'''
		pass
		
	def checkWin(self):
		'''
		Checks whether this player satisfies a win condition.
		'''
		for k in self.builder:
			if k.isActive:
				if k.getTile().getLevel() == 3:
					return True
		
	def checkLose(self):
		'''
		Checks whether this player satisfies a lose condition.
		'''
		canMove = False
		x = []
		y = []
		
		for i in range(5):
			for j in range(5):
				for k in self.builder:
					if k.isActive:
						canMove=canMove or k.canMoveTo(i,j)
				if canMove is True:
					break
			if canMove is True:
				break
				
		return (not canMove)

class NewGame(Widget):
	text = StringProperty('')
	player0 = ObjectProperty(None)
	player1 = ObjectProperty(None)
	player2 = ObjectProperty(None)
	player3 = ObjectProperty(None)
	players = ReferenceListProperty(player0, player1, player2, player3)
	grid = ObjectProperty(None)
	playerCount = NumericProperty(4)
	gPhase = 0
	screen = NumericProperty(4)
	current = NumericProperty(0) #Builder selected
	currentPlayer = NumericProperty(0) #Current Player (0, 1) 0 is named Player1, 1 is Player2
	xP=NumericProperty(0)
	yP=NumericProperty(0)
	heroes = ListProperty(['Bacchus','Mercury','Graeae','Janus','Apollo','Phobos and Deimos','Atlas','Artemis'])
	#Add Active heroes here
	activeHeroes = ['Atlas', 'Artemis']
	hero0 = StringProperty('')
	hero1 = StringProperty('')
	hero2 = StringProperty('')
	drawnHeroes = ReferenceListProperty(hero0, hero1, hero2)
	#buildFX = SoundLoader.load('assets/sound fx/building fx.mp3')
	
	def start(self):
		for i in range(self.playerCount):
			self.players[i].isActive = True
		self.drawHeroes()
		
	def drawHeroes(self):
		drawn = sample(self.heroes,3)
		#Test Heroes
		#drawn = ['Vanilla', 'Vanilla', 'Vanilla']
		for i in range(3):
			self.drawnHeroes[i] = drawn[i]
			
	def saveState(self):
		for player in self.players:
			if player.isActive:
				for builder in player.builder:
					if builder.isActive:
						builder.tileSave = builder.tile
		for y in self.grid.matrix:
			for x in y:
				x.levelSave = x.level
				x.domedSave = x.domed
				x.flagSave = x.flag
				x.ownerSave = x.owner
	
	def loadState(self):
		for y in self.grid.matrix:
			for x in y:
				x.unoccupy()
				x.level = x.levelSave
				x.domed = x.domedSave
				x.flag = x.flagSave
				x.owner = x.ownerSave
		for player in self.players:
			if player.isActive:
				player.skillActive = False
				player.activatedSkill = 0
				for builder in player.builder:
					if builder.isActive:
						builder.tileSave.occupy(builder)
						builder.isSelected = False
		self.gPhase = 1
	
	def restart(self):
		for player in self.players:
			player.hero = 'Vanilla'
			player.isCurrent = False
			player.maxActive = 1
			player.activatedSkill = 0
			for builder in player.builder:
				builder.isSelected = False
				builder.pos = self.width,self.height
				builder.isActive = False
				builder.tile = None
		self.grid.levelUsed = [0,0,0,0]
		for i in self.grid.matrix:
			for tile in i:
				tile.unoccupy()
				tile.domed=False
				tile.level = 0
				tile.unflag()
		self.current = 0
		self.screen = 1
		self.currentPlayer = 0
		self.gPhase = 0
		self.text = ''
	
	def init(self):
		self.grid.setTileGrid()
		for player in self.players:
			player.builder0.isActive = True
			player.builder1.isActive = True
			#Graeae
			#Get an extra Builder
			if player.hero == 'Graeae':
				player.builder2.isActive = True
			##
			
			#Set Skill cap here
			elif player.hero == 'Artemis':
				player.maxActive = 2
				
		self.player0.isCurrent = True
	
	def timer(self,dt):
		if self.grid.timer[0] == 0 and self.grid.timer[1] == 0 and self.grid.timer[2] == 0 and self.grid.timer[3] == 0 and self.grid.timer[4] == 0 and self.grid.timer[5] == 0:
			pass
		else:
			self.grid.timer[3] -= 1
#			if int(self.grid.timer[5]) == -1:
#				self.grid.timer[5] = 9
#				self.grid.timer[4] -= 1
#			if int(self.grid.timer[4]) == -1:
#				self.grid.timer[4] = 9
#				self.grid.timer[3] -= 1
			if int(self.grid.timer[3]) == -1:
				self.grid.timer[3] = 9
				self.grid.timer[2] -= 1
			if int(self.grid.timer[2]) == -1:
				self.grid.timer[2] = 5
				self.grid.timer[1] -= 1
			if int(self.grid.timer[1]) == -1:
				self.grid.timer[1] = 9
				self.grid.timer[0] -= 1
			pass
			
	def place(self, builder):
		self.grid.getTile(self.xP, self.yP).occupy(builder)
		builder.setTile(self.grid.getTile(self.xP, self.yP))
		builder.pos = builder.tile.pos
		self.current += 1
	
	def build(self):
		
		#Atlas
		#If skill is Active, build a dome instead
		if self.players[self.currentPlayer].hero == 'Atlas' and self.players[self.currentPlayer].skillActive:
			self.grid.getTile(self.xP, self.yP).dome()
		##
			
		else:
			self.grid.getTile(self.xP, self.yP).build()
		self.players[self.currentPlayer].builder[self.current].isSelected = False
		#Adds or Removes a flag on the selected GridTile
		if self.grid.getTile(self.xP, self.yP).isDomed():
			self.grid.getTile(self.xP, self.yP).flag = 0
			self.grid.getTile(self.xP, self.yP).owner = None
		else:
			self.grid.getTile(self.xP, self.yP).flag = self.currentPlayer + 1
			self.grid.getTile(self.xP, self.yP).owner = self.players[self.currentPlayer]
	
	def on_touch_up(self, touch):
		if self.screen == 0:
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
				if self.optionsButton.collide_point(touch.x,touch.y):
					#self.restart()
					#self.loadState()
					self.screen = 2
				elif self.undoTurnButton.x<=touch.x<=self.undoTurnButton.x+self.undoTurnButton.width and self.undoTurnButton.y<=touch.y<=self.undoTurnButton.y+self.undoTurnButton.height:
					self.loadState()
					
				elif self.endTurnButton.x<=touch.x<=self.endTurnButton.x+self.endTurnButton.width and self.endTurnButton.y<=touch.y<=self.endTurnButton.y+self.endTurnButton.height and self.gPhase == 5:
					##Add End of Turn effects here
					
					#Phobos and Deimos
					#Kill any enemy Builder bordering both your builders
					if self.players[self.currentPlayer].hero == 'Phobos and Deimos':
						for k in self.players[(self.currentPlayer + 1)%2].builder:
							if k.isActive:
								if k.isBorderingEnemyBuilder(2):
									k.die()
					##
					
					####
					
					#Deactivates skill
					if self.players[self.currentPlayer].hero in self.activeHeroes:
						self.players[self.currentPlayer].activatedSkill = 0
						self.players[self.currentPlayer].skillActive = False
						
					#Switches to next Player
					self.gPhase = 1
					self.players[self.currentPlayer].isCurrent = False
					self.currentPlayer = (self.currentPlayer + 1) % self.playerCount
					self.players[self.currentPlayer].isCurrent = True
					self.grid.timer = [0,2,0,0,0,0]
					self.saveState()
					#Checks if current Player can no longer move
					if self.players[self.currentPlayer].checkLose():
						self.text = 'PLAYER '+str((self.currentPlayer + 1)%self.playerCount +1)+' WINS!'
						self.gPhase =4
				
				#Prevents Passive heroes from using the skill button
				elif self.players[self.currentPlayer].hero not in self.activeHeroes:
					pass
				elif self.players[self.currentPlayer].activatedSkill >= self.players[self.currentPlayer].maxActive:
					pass
				elif self.powerButton.collide_point(touch.x,touch.y):
					
					#Skill Deactivate
					if self.players[self.currentPlayer].skillActive:
						self.players[self.currentPlayer].skillActive = False
						
						if self.players[self.currentPlayer].hero == 'Artemis' and self.gPhase == 2 and self.players[self.currentPlayer].activatedSkill == 1:
							self.gPhase = 3
							self.players[self.currentPlayer].activatedSkill -= 1
					
					#Skill Activate
					else:
						self.players[self.currentPlayer].skillActive = True
						
						if self.players[self.currentPlayer].hero == 'Artemis' and self.gPhase == 3:
							self.gPhase = 2
							self.players[self.currentPlayer].activatedSkill += 1
			
			#Initial Phase
			elif self.gPhase == 0:
				if not self.grid.getTile(self.xP, self.yP).isOccupied():
					if self.currentPlayer < self.playerCount:
						if self.players[self.currentPlayer].builder[self.current].isActive:
							self.place(self.players[self.currentPlayer].builder[self.current])
							if not self.players[self.currentPlayer].builder[self.current].isActive:
								self.current = 0
								self.players[self.currentPlayer].isCurrent = False
								self.currentPlayer += 1
								self.players[self.currentPlayer%self.playerCount].isCurrent = True
					if self.currentPlayer == self.playerCount:
						self.grid.timer = [0,2,0,0,0,0]
						self.currentPlayer = 0
						self.current = 0
						self.gPhase = 1
						self.saveState()
	
					
			#Choose  Phase
			elif self.gPhase == 1:
				if self.grid.getTile(self.xP, self.yP).isOccupied():
					if self.grid.getTile(self.xP, self.yP).getOccupier().getPlayer().num == self.currentPlayer:
						self.grid.getTile(self.xP,self.yP).getOccupier().isSelected = True
						self.current = self.grid.getTile(self.xP, self.yP).getOccupier().getNum()
						self.gPhase = 2
				pass
			
			#Move Phase
			elif self.gPhase == 2:
				#Checks if selected tile contains the selected Builder
				if self.players[self.currentPlayer].builder[self.current].getTile().getX()==self.xP and self.players[self.currentPlayer].builder[self.current].getTile().getY()==self.yP:
					self.grid.getTile(self.xP,self.yP).getOccupier().isSelected = False
					self.gPhase = 1
				#Checks if the selected tile contains a Builder owned by the current Player
				elif self.grid.getTile(self.xP, self.yP).isOccupied():
					if self.grid.getTile(self.xP, self.yP).getOccupier().getPlayer().num == self.currentPlayer:
						self.players[self.currentPlayer].builder[self.current].isSelected = False
						self.grid.getTile(self.xP,self.yP).getOccupier().isSelected = True
						self.current = self.grid.getTile(self.xP, self.yP).getOccupier().getNum()
				#Checks if the selected Builder can move to the selected tile
				if self.players[self.currentPlayer].builder[self.current].moveBuilder(self.xP, self.yP):
					
					#Artemis
					#Checks if skill is Active and has not been used yet.
					#If Yes, move again
					if self.players[self.currentPlayer].hero == 'Artemis' and self.players[self.currentPlayer].skillActive:
						if self.players[self.currentPlayer].activatedSkill == 0:
							self.players[self.currentPlayer].activatedSkill += 2
							self.players[self.currentPlayer].skillActive = False
							self.gPhase = 2
						else: 
							self.players[self.currentPlayer].activatedSkill += 1
							self.players[self.currentPlayer].skillActive = False
							self.gPhase = 3
					##
					
					else:
						self.gPhase = 3
					#Checks if the current Player won by moving
					if self.players[self.currentPlayer].checkWin():
						self.text = 'PLAYER '+str(self.currentPlayer + 1)+' WINS!'
						self.gPhase = 4
				
			#Build Phase
			elif self.gPhase ==3:
				#Checks if the selected Builder can build on the selected GridTile
				valid = False
				
				#Graeae
				#You can use any of your Builder to build
				if self.players[self.currentPlayer].hero == 'Graeae':
					for k in self.players[self.currentPlayer].builder:
						if k.isActive:
							if k.canBuildOn(self.xP, self.yP):
								valid = True
								break
				##
							
				elif self.players[self.currentPlayer].builder[self.current].canBuildOn(self.xP, self.yP):
					valid = True
				if valid:
					self.build()
					self.gPhase = 5
					#End of current Player's Turn
					
			elif self.gPhase == 5:
				pass
					
			elif self.gPhase == 4:
				self.restart()
				self.screen = 4
				self.text = ''
				
		elif self.screen == 1:
			valid = False
			if self.drawn0.collide_point(touch.x,touch.y):
				self.players[self.currentPlayer].hero = self.hero0
				valid = True
			elif self.drawn1.collide_point(touch.x,touch.y):
				self.players[self.currentPlayer].hero = self.hero1
				valid = True
			elif self.drawn2.collide_point(touch.x,touch.y):
				self.players[self.currentPlayer].hero = self.hero2
				valid = True
			if valid:
				self.players[self.currentPlayer].isCurrent = False
				self.currentPlayer += 1
				self.players[self.currentPlayer%self.playerCount].isCurrent = True
				self.drawHeroes()
				if self.currentPlayer == self.playerCount:
					self.currentPlayer = 0
					self.init()
					self.screen = 0
					
		elif self.screen == 2:
			if self.closeOptionsButton.collide_point(touch.x,touch.y):
				self.screen = 0
			elif self.settingsButton.collide_point(touch.x,touch.y):
				self.screen = 3
				
		elif self.screen == 3:
			if self.closeSettingsButton.collide_point(touch.x,touch.y):
				self.screen = 2
		elif self.screen == 4:
			if self.startGame.collide_point(touch.x,touch.y):
#				self.restart()
				self.screen = 1
			elif self.gameOptionsButton.collide_point(touch.x,touch.y):
				self.screen = 5
		elif self.screen == 5:
			if self.closeGameOptionsButton.collide_point(touch.x,touch.y):
				self.screen = 4
			pass
			
class GameButton(ButtonBehavior, Widget):
	def __init__(self, **kwargs):
		super(GameButton, self).__init__(**kwargs)
		
class GameCircleButton(ButtonBehavior, Widget):
	def __init__(self, **kwargs):
		super(GameCircleButton, self).__init__(**kwargs)
	def collide_point(self, x, y):
		if (self.width/2)**2 >= (x - (self.x+self.width/2))**2 + (y - (self.y+self.width/2))**2:
			return True
		return False
		

class NewApp(App):

    def build(self):
    	game = NewGame()
    	game.start()
    	timer = Clock.schedule_interval(game.timer, 1)
    	return game
    	
    def on_pause(self):
    	return True
    	
    def on_stop(self):
    	return True


if __name__ in ('__main__','__android__'):
    NewApp().run()
