from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior

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
