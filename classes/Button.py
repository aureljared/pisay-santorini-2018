from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior, ToggleButtonBehavior
from kivy.properties import StringProperty

class GameButton(ButtonBehavior, Widget):
    source = StringProperty('')
    def __init__(self, **kwargs):
        super(GameButton, self).__init__(**kwargs)
        self.source = 'blank.png'
    def on_state(self, widget, value):
        if value == 'down':
            pass
            self.source = 'drawables/buttons/onclick highlight bare.png'
        else:
            pass
            self.source = 'blank.png'
        
class GameCircleButton(ButtonBehavior, Widget):
    source = StringProperty('')
    def __init__(self, **kwargs):
        super(GameCircleButton, self).__init__(**kwargs)
        self.source = 'blank.png'
    def on_state(self, widget, value):
        if value == 'down':
            pass
            self.source = 'drawables/buttons/button push.png'
        else:
            pass
            self.source = 'blank.png'
    def collide_point(self, x, y):
        if (self.width/2)**2 >= (x - (self.x+self.width/2))**2 + (y - (self.y+self.width/2))**2:
            return True
        return False

class GameToggleButton(ToggleButtonBehavior, Widget):
    source = StringProperty('')
    def __init__(self, **kwargs):
        super(GameToggleButton, self).__init__(**kwargs)
        self.source = 'drawables/buttons/switch full hitbox.png'
    def on_state(self, widget, value):
        if value == 'down':
            pass
            self.source = 'drawables/buttons/switch flipped hitbox.png'
        else:
            pass
            self.source = 'drawables/buttons/switch full hitbox.png'
