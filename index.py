# Make a default starting value for resource dictionary
resourceDictionary = {"stone": [50, 3], "wood": [50, 3], "clay": [50, 3], "hide": [50, 3], "gold": [50, 3], "workers": [10, 3]}

# Building Index, contains all the buildings of a  village
buildingIndex = [None] * 10
buildingIndex[0] = ["Stone Quarry", "A large quarry for gathering stone", 0]
buildingIndex[1] = ["Lumbermill", "A large quarry for gathering stone", 0]
buildingIndex[2] = ["Stone Quarry", "A large quarry for gathering stone", 0]
buildingIndex[3] = ["Stone Quarry", "A large quarry for gathering stone", 0]
buildingIndex[4] = ["Stone Quarry", "A large quarry for gathering stone", 0]
buildingIndex[5] = ["Stone Quarry", "A large quarry for gathering stone", 0]

# Upgrade Index - Statically holds the costs of all buildings and upgrades
upgradeIndex = [[None for width in range(5)] for height in range(10)]
upgradeIndex[0][0] = ({"stone": 5, "wood": 5}, {"wood": 2}, 0)
upgradeIndex[0][1] = ({"stone": 10, "wood": 10}, {"wood": 2}, 1)
upgradeIndex[0][2] = ({"stone": 15, "wood": 15}, {"wood": 3}, 2)

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
