import kivy
kivy.require('1.9.2')

from kivy.config import Config
Config.read('config.ini')
#Config.set('modules','screen','onex, portrait')
Config.write()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock
from kivy.graphics import *

from classes.Game import Game
from classes.Builder import Builder
from classes.Button import GameButton, GameCircleButton
from classes.Grid import Grid
from classes.GridTile import GridTile
from classes.Player import Player

class SantoriniApp(App):
    def build(self):
    	game = Game()
    	game.start()
    	timer = Clock.schedule_interval(game.timer, 1)
    	return game
    	
    def on_pause(self):
    	return True
    	
    def on_stop(self):
    	return True

if __name__ in ('__main__','__android__'):
	#sound = SoundLoader.load("assets/sound fx/win fx.mp3")
    SantoriniApp().run()
