Version: alpha0.1.4

Updates from previous version:
	Fixed Building bug

Working grid
Game doesn't restart
Will have to fix builder placement order
Panels: no interactions yet (the top panel is only an image)


For Hero implementation:
Add Heroes as you wish
Built functions for checking surrounding or bordering

To test:
	In New.kv:
		Find Player Initialization
		Change any of the Players' hero attribute
	Run main.py
	
Sample Heroes
Bacchus:
	Enemy Builders adjacent to your Builders cannot move vertically or horizontally

Mercury:
	When your Builders are adjacent to a GridTile with your Flag, they gain +1 movement range
	
Gaeae:
	Get an extra Builder
	During Build Phase, any of your Builders may be used to build
	
Janus:
	Your Builder may move to another tile Bordering your other builders
	
Apollo:
	Your Builder may Move onto an Enemy Builder's space by forcing their Builder to move to the space you just vacated