import resource

# Print the stock amount of each resource
def stockAmount(resDict):
    print("Resource Stock Amount -")
    for key in resDict:
        print(("  {0}: {1}").format(key.title(), str(resource.getStockAmount(resDict, key))))
    print()

# Print the details of an upgrade after upgrading a building
def upgradeDetails(buildId, buildIndex):
    if buildIndex[buildId][2] == 1:
        print(("You have built a {}!\n").format(buildIndex[buildId][0]))
    else:
        print((("You upgraded your {0} to tier {1}!\n").format(buildIndex[buildId][0], buildIndex[buildId][2])))

# Print all currently build buildings and their stats
def buildingList(buildIndex):
    print("Building List - ")
    for building in buildIndex:
        if (building != None) and (building[2] != 0):
            print(("  Tier {0} {1} - {2}").format(str(building[2]), building[0], building[1]))
    print()

# Prints out the details of an unlocked technology
def techUnlockDetails(techId, techIndex):
    print(("You have unlocked {0}\n").format(techIndex[techId][0]))

# Prints out the currently researched technology
def techTree(techIndex):
    print("Technology Researched - ")
    for tech in techIndex:
        if (tech != None) and (tech[2] != 0):
            print(("  {0} - {1}").format(tech[0], tech[1]))
    print()