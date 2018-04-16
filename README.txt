Version: alpha0.1.7

Updates from previous version:
	Added Game menus
	Added 2-4 player support
	implemented End Turn and Undo Move

Need:
	Feddback Mechanism (Game Texts)
	Game SetUp
	Toggles in Settings
	Concede and Quit Game in Options

Notes:
	Bacchus op
	Janus noob

Draw Phase
Game Phase
Game doesn't restart
Panels: no interactions yet (the top panel is only an image)


For Hero implementation:
	Add Heroes as you wish
	For Athena: 
		I suggest you use skillActive in Player for when any of your Builder moves up.
		Then do the check on opponents turn (Similar to Bacchus) for skillActive
	For Pan: 
		I suggest you use skillActive in Player for when any of your Builder moves down two levels.
		Then add a check in checkWin() in Player for skillActive
	For Hephaestus:
		Append Hephaestus to active heroes.
		Before #End of current Player's Turn:
			If skillActive and selected GridTile.level < 3:
				build()
	For Prometheus:
		Append Prometheus to active heroes.
		Set maxActive in NewGame.start()
		In #Skill Activate:
			set to Build Phase
		In #Build Phase:
			Before #End of current Player's Turn:
				Do similar to #Artemis
		In #Skill Deactivate:
			set to Move Phase
		In canMoveTo() inBuilder:
			If activatedSkill is equal to maxActive:
				Movkng up is invalid
				

To add active heroes:
	In main.py:
		Find: #Add Active heroes here
		Append your hero to: activeHeroes

To test:
	In main.py:
		Find #Test heroes
		Comment out: drawn = sample(self.heroes,3)
		Uncomment: #drawn = ['Apollo', 'Artemis', 'Atlas']
		Modify elements to heroes you want to test
		NOTE: this list needs to have a length of 3
	Run main.py
	
Sample Heroes
Bacchus:
	Enemy Builders adjacent to your Builders cannot move vertically or horizontally

Mercury:
	When your Builders are adjacent to a GridTile with your Flag, they gain +1 movement range
	
Graeae:
	Get an extra Builder
	During Build Phase, any of your Builders may be used to build
	
Janus:
	Your Builder may move to another tile Bordering your other builders
	
Apollo:
	Your Builder may Move onto an Enemy Builder's space by forcing their Builder to move to the space you just vacated
	
Phobos and Deimos:
	At the end of your turn, kill enemy Builders bordering two of your Builders.
	
Atlas:
	Your Builder may build a dome at any level
	
Artemis:
	Your Builder may move one additional time, (but not back to its original space #Haven't implemented yet)