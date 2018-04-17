from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, BooleanProperty, StringProperty

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
