from kivy.uix.widget import Widget
from kivy.properties import ReferenceListProperty, ListProperty, ObjectProperty

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
    timer = ListProperty([0,0,0,0])
    
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
