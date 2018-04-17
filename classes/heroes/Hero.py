class Hero():
    heroes = []

    def __init__(self):
        self.heroes.append('Bacchus')
        self.heroes.append('Mercury')
        self.heroes.append('Graeae')
        self.heroes.append('Janus')
        self.heroes.append('Apollo')
        self.heroes.append('Phobos and Deimos')
        self.heroes.append('Atlas')
        self.heroes.append('Artemis')
        self.heroes.append('Hephaestus')

    def getAvailableHeroes(self):
        return self.heroes