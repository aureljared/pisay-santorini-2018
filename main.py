import kivy
kivy.require('1.9.2')

from kivy.config import Config
Config.read('config.ini')
Config.set('modules','screen','ipad,portrait')
Config.write()
from random import randint
from random import sample
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
	tile=ObjectProperty(None, allownone = True)
	isSelected=BooleanProperty(False)
	isActive=BooleanProperty(True)
	
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
		
	def isBorderingEnemyBuilder(self, count):
		x = int(self.tile.getX())
		y = int(self.tile.getY())
		n = 0
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if i != 0 and j != 0:
					pass
				elif x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.tile.getGrid().getTile(x + i, y + j).isOccupied():
					if self.tile.getGrid().getTile(x + i, y + j).getOccupier().player.num != self.player.num:
						n += 1
					if n == count:
						return True
		return False
	
	def die(self):
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
			if self.isAdjacentToEnemyBuilder():
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
	
	#EDIT
	#May need check methods similar to those in Builder
	
	def isBorderingBuilder(self, num):
		x = int(self.getX())
		y = int(self.getY())
		
		for i in (-1,0,1):
			for j in (-1,0,1):
				if i != 0 and j != 0:
					pass
				elif x+i ==-1 or y+j == -1 or x+i == 5 or y+j == 5:
					pass
				elif self.getGrid().getTile(x + i, y + j).isOccupied():
					if self.getGrid().getTile(x + i, y + j).getOccupier().player.num == num:
						return True
		return False
		
	##
	
	def build(self):
		if self.level < 3:
			self.level += 1
			self.grid.tileUsed(self.level)
		elif self.domed is False:
			self.dome()
		else:
			raise Exception
			
	def dome(self):
		self.grid.tileUsed(4)
		self.domed = True
			
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
		builder.pos = self.pos
		
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
	timer = ListProperty([0,0,0,0,0,0])
	
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
		pass
		
	def build(self):
		pass
		
	def checkWin(self):
		for k in self.builder:
			if k.isActive:
				if k.getTile().getLevel() == 3:
					return True
		
	def checkLose(self):
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
	players = ReferenceListProperty(player0, player1)
	grid = ObjectProperty(None)
	gPhase = 0
	screen = NumericProperty(1)
	current = NumericProperty(0) #Builder selected
	player = NumericProperty(0) #Current Player (0, 1) 0 is named Player1, 1 is Player2
	xP=NumericProperty(0)
	yP=NumericProperty(0)
	builder00=ObjectProperty(None)
	builder01=ObjectProperty(None)
	builder10=ObjectProperty(None)
	builder11=ObjectProperty(None)
	builder02=ObjectProperty(None)
	builder03=ObjectProperty(None)
	builder12=ObjectProperty(None)
	builder13=ObjectProperty(None)
	builder = ReferenceListProperty(builder00, builder01, builder10, builder11,builder02, builder03, builder12, builder13)
	heroes = ListProperty(['Bacchus','Mercury','Graeae','Janus','Apollo','Phobos and Deimos','Atlas','Artemis'])
	#Add Active heroes here
	activeHeroes = ['Atlas', 'Artemis']
	hero0 = StringProperty('')
	hero1 = StringProperty('')
	hero2 = StringProperty('')
	drawnHeroes = ReferenceListProperty(hero0, hero1, hero2)
	
	def drawHeroes(self):
		drawn = sample(self.heroes,3)
		#Test Heroes
		#drawn = ['Apollo', 'Artemis', 'Atlas']
		for i in range(3):
			self.drawnHeroes[i] = drawn[i]
	
	def start(self):
		self.drawHeroes()
	
	def init(self):
		self.grid.setTileGrid()
		for player in self.players:
			
			#Graeae
			#Get an extra Builder
			if player.hero == 'Graeae':
				player.builder2.isActive = True
			##
			
			#Set Skill cap here
			elif player.hero == 'Artemis':
				player.maxActive = 1
				
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
		if self.players[self.player].hero == 'Atlas' and self.players[self.player].skillActive:
			self.grid.getTile(self.xP, self.yP).dome()
		##
			
		else:
			self.grid.getTile(self.xP, self.yP).build()
		self.builder[self.current].isSelected = False
		#Adds or Removes a flag on the selected GridTile
		if self.grid.getTile(self.xP, self.yP).isDomed():
			self.grid.getTile(self.xP, self.yP).flag = 0
			self.grid.getTile(self.xP, self.yP).owner = None
		else:
			self.grid.getTile(self.xP, self.yP).flag = self.player + 1
			self.grid.getTile(self.xP, self.yP).owner = self.players[self.player]
	
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
				#Prevents Passive heroes from using the skill button
				if self.players[self.player].hero not in self.activeHeroes:
					pass
				elif self.players[self.player].activatedSkill >= self.players[self.player].maxActive:
					pass
				elif (self.powerButton.width/2)**2 >= (touch.x - (self.powerButton.x+self.powerButton.width/2))**2 + (touch.y - (self.powerButton.y+self.powerButton.width/2))**2:
					
					#Skill Deactivate
					if self.players[self.player].skillActive:
						self.players[self.player].skillActive = False
					
					#Skill Activate
					else:
						self.players[self.player].skillActive = True
			
			#Initial Phase
			elif self.gPhase == 0:
				if not self.grid.getTile(self.xP, self.yP).isOccupied():
					if self.player < 2:
						if self.players[self.player].builder[self.current].isActive:
							self.place(self.players[self.player].builder[self.current])
							if not self.players[self.player].builder[self.current].isActive:
								self.current = 0
								self.players[self.player].isCurrent = False
								self.player += 1
								self.players[self.player%2].isCurrent = True
					if self.player == 2:
						self.grid.timer = [0,2,0,0,0,0]
						self.player = 0
						self.current = 0
						self.gPhase = 1
	
					
			#Choose  Phase
			elif self.gPhase == 1:
				if self.grid.getTile(self.xP, self.yP).isOccupied():
					if self.grid.getTile(self.xP, self.yP).getOccupier().getPlayer().num == self.player:
						self.grid.getTile(self.xP,self.yP).getOccupier().isSelected = True
						self.current = self.grid.getTile(self.xP, self.yP).getOccupier().getNum()
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
						self.builder[self.current].isSelected = False
						self.grid.getTile(self.xP,self.yP).getOccupier().isSelected = True
						self.current = self.grid.getTile(self.xP, self.yP).getOccupier().getNum()
				#Checks if the selected Builder can move to the selected tile
				if self.builder[self.current].moveBuilder(self.xP, self.yP):
					
					#Artemis
					#Checks if skill is Active and has not been used yet.
					#If Yes, move again
					if self.players[self.player].hero == 'Artemis' and self.players[self.player].skillActive and self.players[self.player].activatedSkill < 1:
						self.players[self.player].skillActive = False
						self.players[self.player].activatedSkill += 1
						self.gPhase = 2
					##
					
					else:
						self.gPhase = 3
					#Checks if the current Player won by moving
					if self.players[self.player].checkWin():
						self.text = 'PLAYER '+str(self.player + 1)+' WINS!'
						self.gPhase = 4
				
			#Build Phase
			elif self.gPhase ==3:
				#Checks if the selected Builder can build on the selected GridTile
				valid = False
				
				#Graeae
				#You can use any of your Builder to build
				if self.players[self.player].hero == 'Graeae':
					for k in self.players[self.player].builder:
						if k.isActive:
							if k.canBuildOn(self.xP, self.yP):
								valid = True
								break
				##
							
				elif self.builder[self.current].canBuildOn(self.xP, self.yP):
					valid = True
				if valid:
					self.build()
					#End of current Player's Turn
					
					##Add End of Turn effects here
					
					#Phobos and Deimos
					#Kill any enemy Builder bordering both your builders
					if self.players[self.player].hero == 'Phobos and Deimos':
						for k in self.players[(self.player + 1)%2].builder:
							if k.isActive:
								if k.isBorderingEnemyBuilder(2):
									k.die()
					##
					
					
					####
					
					#Deactivates skill
					if self.players[self.player].hero in self.activeHeroes:
						self.players[self.player].activatedSkill = 0
						self.players[self.player].skillActive = False
						
					#Switches to next Player
					self.gPhase = 1
					self.players[self.player].isCurrent = False
					self.player = (self.player + 1) % 2
					self.players[self.player].isCurrent = True
					self.grid.timer = [0,2,0,0,0,0]
					#Checks if current Player can no longer move
					if self.players[self.player].checkLose():
						self.text = 'PLAYER '+str((self.player + 1)%2 +1)+' WINS!'
						self.gPhase =4
					
			elif self.gPhase == 4:
				pass
				
		if self.screen == 1:
			valid = False
			if self.drawn0.x <= touch.x <= self.drawn0.x + self.drawn0.width and self.drawn0.y <= touch.y <= self.drawn0.y + self.drawn0.height:
				self.players[self.player].hero = self.hero0
				valid = True
			elif self.drawn1.x <= touch.x <= self.drawn1.x + self.drawn1.width and self.drawn1.y <= touch.y <= self.drawn1.y + self.drawn1.height:
				self.players[self.player].hero = self.hero1
				valid = True
			elif self.drawn2.x <= touch.x <= self.drawn2.x + self.drawn2.width and self.drawn2.y <= touch.y <= self.drawn2.y + self.drawn2.height:
				self.players[self.player].hero = self.hero2
				valid = True
			if valid:
				self.players[self.player].isCurrent = False
				self.player += 1
				self.players[self.player%2].isCurrent = True
				self.drawHeroes()
				if self.player == 2:
					self.player = 0
					self.init()
					self.screen = 0

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