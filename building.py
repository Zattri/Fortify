# Main upgrade function -
# Check if the upgrade can be afforded
# If so pay the cost, increment the upgrade tier
# If not print error
def upgradeBuilding(buildId, buildIndex, upgradeIndex, resDict):
    if buildIndex[buildId] != None:
        upgDict = getUpgradeCost(buildId, buildIndex[buildId][2], upgradeIndex)
        if checkUpgradeCost(upgDict, resDict):
            resDict = payUpgradeCost(upgDict, resDict)
            buildIndex = incrementUpgradeTier(buildId, buildIndex)
            # Check if resource gather amount needs upgrading
            printUpgradeDetails(buildId, buildIndex)
        else:
            print("You cannot afford the cost of this upgrade")
    return (resDict, buildIndex)

# Return the upgrade cost dictionary from the upgradeIndex
def getUpgradeCost(buildId, upgTier, upgradeIndex):
    return upgradeIndex[buildId][upgTier]

# Check if can afford the cost of an upgrade using the upgrade cost dict and resource dict
def checkUpgradeCost(upgDict, resDict):
    canAfford = True
    for key in upgDict:
        if  upgDict[key] > resDict[key][0]:
            canAfford = False
    return canAfford

# Deduct the cost of the upgrade from the resource dict
def payUpgradeCost(upgDict, resDict):
    for key in upgDict:
        resDict.update({key: [(resDict[key][0] - upgDict[key]), resDict[key][1]]})
    return resDict

# Increment the upgrade tier of the appropriate building up by 1
def incrementUpgradeTier(buildId, buildIndex):
    buildIndex[buildId] = (buildIndex[buildId][0], buildIndex[buildId][1], (buildIndex[buildId][2] + 1))
    return buildIndex

# Print all currently build buildings and their stats
def printBuildings(buildIndex):
    print("Building List - ")
    for building in buildIndex:
        if (building != None) and (building[2] != 0):
            print(("Tier {0} {1} - {2}").format(str(building[2]), building[0], building[1]))
    print()

# Print the details of an upgrade after upgrading a building
def printUpgradeDetails(buildId, buildIndex):
    if buildIndex[buildId][2] == 1:
        print(("You have built a {}!\n").format(buildIndex[buildId][0]))
    else:
        print((("You upgraded your {0} to tier {1}!\n").format(buildIndex[buildId][0], buildIndex[buildId][2])))
