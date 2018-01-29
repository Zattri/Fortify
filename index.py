# Building Index, contains all the buildings of a  village
buildingIndex = [None] * 10
buildingIndex[0] = ("Village Hut", "A hut for housing extra workers", 0)

# Upgrade Index - Staticly holds the costs of all buildings and upgrades
upgradeIndex = [[None for width in range(5)] for height in range(10)]
upgradeIndex[0][0] = {"stone": 5, "wood": 5}
upgradeIndex[0][1] = {"stone": 10, "wood": 10}
upgradeIndex[0][2] = {"stone": 15, "wood": 15}
