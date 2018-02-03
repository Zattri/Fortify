# Make a default starting value for resource dictionary
resourceDictionary = {"stone": [50, 3], "wood": [50, 3], "clay": [50, 3], "hide": [50, 3], "gold": [50, 3], "workers": [30, 2]}

# Building Index, contains all the buildings of a  village
buildingIndex = [None] * 10
buildingIndex[0] = ["Stone Quarry", "A large quarry, used for gathering stone", 0]
buildingIndex[1] = ["Lumber yard", "A yard for woodcutters to process and store wood", 0]
buildingIndex[2] = ["Clay Pit", "Wet flatland, perfect for harvesting clay", 0]
buildingIndex[3] = ["Hunter's Lodge", "A small wooden hut, occupied by hunters of various pelts hide", 0]
buildingIndex[4] = ["Gold Mine", "A deep mine, maybe there's some gold in it still", 0]
buildingIndex[5] = ["Farm", "Rich fertile soil ideal for farming and increasing workers", 0]

# Upgrade Index - Statically holds the costs of all buildings and upgrades
upgradeIndex = [[None for width in range(5)] for height in range(10)]
upgradeIndex[0][0] = ({"clay": 5, "wood": 5, "workers": 3}, {"stone": 2}, None)
upgradeIndex[1][0] = ({"stone": 5, "hide": 5, "workers": 3}, {"wood": 2}, None)
upgradeIndex[2][0] = ({"hide": 5, "wood": 5, "workers": 3}, {"clay": 2}, None)
upgradeIndex[3][0] = ({"stone": 5, "wood": 5, "workers": 3}, {"hide": 2}, None)
upgradeIndex[4][0] = ({"clay": 5, "stone": 5, "workers": 3}, {"gold": 2}, None)
upgradeIndex[5][0] = ({"hide": 5, "clay": 5, "workers": 3}, {"workers": 1}, None)

# Quarry Upgrades
upgradeIndex[0][1] = ({"stone": 10, "wood": 10}, {"stone": 2}, 1)
upgradeIndex[0][2] = ({"stone": 15, "wood": 15}, {"stone": 3}, 2)

techIndex = [None] * 10
techIndex[0] = ["Forged Armour", "Forge armour to increase troop defence", 0]
techIndex[1] = ["Forged Tools", "Create tools to increase gathering rate", 0]
techIndex[2] = ["Herbalist Training", "Train workers to become Herbalists", 0]
techIndex[3] = ["Recruit Training", "Train workers to become military recruits", 0]

'''
Building Ideas - 
Quarry - Stone
Lumbermill - Wood
Clay Pit - Clay
Hunter's Lodge - Hide
Mine - Gold?
Farm - For food / growth rate

Unit Buildings - 
Trading Post - Mercenaries
Garrison - Infantry
Barracks - More Infantry?


Mercenary Ideas - 
Hired Sword -
Roaming Wizard - 

'''
