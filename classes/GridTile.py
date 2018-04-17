from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, BooleanProperty, ObjectProperty, ReferenceListProperty, StringProperty

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
