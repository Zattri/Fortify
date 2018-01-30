import output
# Main upgrade function -
# Check if the upgrade can be afforded
# If so pay the cost, increment the upgrade tier
# If not print error
def upgradeBuilding(buildId, buildIndex, upgradeIndex, techIndex, resDict):
    if buildIndex[buildId] != None:
        upgDict, gatherDict, techId = getUpgradeIndex(buildId, buildIndex[buildId][2], upgradeIndex)
        # Get gather amount update
        # Get techId to unlock
        if checkUpgradeCost(upgDict, resDict):
            resDict = payUpgradeCost(upgDict, resDict)
            buildIndex = incrementUpgradeTier(buildId, buildIndex)
            techIndex = checkTechUnlock(techId, techIndex)
            resDict = checkGatherIncrease(gatherDict, resDict)
            output.upgradeDetails(buildId, buildIndex)
            output.techUnlockDetails(techId, techIndex)
        else:
            print("You cannot afford the cost of this upgrade")
    return (resDict, buildIndex, techIndex)

# Return the upgrade cost dictionary from the upgradeIndex
def getUpgradeIndex(buildId, upgTier, upgradeIndex):
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

# Unlocks a part of the technology tree
def checkTechUnlock(techId, techIndex):
    if techId != None:
        techIndex[techId][2] = 1
    return techIndex

# Checks if a resource gather rate should be increased and applies that increase
def checkGatherIncrease(gatherDict, resDict):
    if gatherDict != None:
        for key in gatherDict:
            resDict.update({key: [resDict[key][0], (resDict[key][1] + gatherDict[key])]})
    return resDict