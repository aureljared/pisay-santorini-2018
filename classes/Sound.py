from kivy.core.audio import SoundLoader, Sound

class Sounds:
    def __init__(self):
        self.SFX = {}
        self.BGM = {}
        self.bgmOn = {}
        self.volume = 1
    def add(self,filename,filetype = "mp3",soundType = "SFX"):
        sound = SoundLoader.load(filename+"."+filetype)
        if soundType == "SFX":
            self.SFX.update({filename:sound})
            self.SFX[filename].volume = self.volume
        else:
            self.BGM.update({filename:sound})
            self.soundOn.update({filename:False})
    def playSound(self,filename):
        if filename in self.SFX:
            self.SFX[filename].play()
        for val in self.BGM:
            if filename != val:
                self.BGM[val].loop = False
                self.BGM[val].volume = 0
                self.bgmOn.update({val:False})
            else:
                self.BGM[val].loop = True
                self.BGM[val].volume = self.volume
                self.bgmOn[val].update({True})
                self.BGM[val].play()
    def updateVolume(vol):
        self.volume = vol
        for val in self.SFX:
            self.SFX[val].volume = self.volume
        for val in self.BGM:
            if self.bgmOn[val] == True:
                self.BGM[val].volume = self.volume
