from kivy.uix.widget import Widget
from kivy.properties import ReferenceListProperty, ListProperty, ObjectProperty, StringProperty, NumericProperty
#from kivy.core.sound import SoundLoader
from random import sample

class Game(Widget):
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
#           if int(self.grid.timer[5]) == -1:
#               self.grid.timer[5] = 9
#               self.grid.timer[4] -= 1
#           if int(self.grid.timer[4]) == -1:
#               self.grid.timer[4] = 9
#               self.grid.timer[3] -= 1
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
#               self.restart()
                self.screen = 1
            elif self.gameOptionsButton.collide_point(touch.x,touch.y):
                self.screen = 5
        elif self.screen == 5:
            if self.closeGameOptionsButton.collide_point(touch.x,touch.y):
                self.screen = 4
            pass
