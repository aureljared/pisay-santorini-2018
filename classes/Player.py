from kivy.uix.widget import Widget
from kivy.properties import ReferenceListProperty, ListProperty, ObjectProperty, BooleanProperty, StringProperty, NumericProperty

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
