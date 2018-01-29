# Gets the stock amount of a resource
def getStockAmount(resDict, dictKey):
    return resDict[dictKey][0]

# Gets the gathering amount of a resource
def getGatherAmount(resDict, dictKey):
    return resDict[dictKey][1]

# Gather a resource of any type, increasing the stock amount of that resource by the gather amount
def updateStock(resDict, dictKey):
    resDict.update({dictKey: [(resDict[dictKey][0] + resDict[dictKey][1]), resDict[dictKey][1]]})
    return resDict

# Gather every resource, increasing the stock amount by the gather amount
def updateAllStock(resDict):
    for key in resDict:
        resDict.update({key: [(resDict[key][0] + resDict[key][1]), resDict[key][1]]})
    return resDict

# Increase the gather amount of a resource by a specified value
def increaseGatherAmount(resDict, dictKey, gatherIncrease):
    resDict.update({dictKey: [resDict[dictKey][0], (resDict[dictKey][1] + gatherIncrease)]})
    return resDict

# Print the stock amount of each resource
def printStockAmount(resDict):
    print("Resource Stock Amount -")
    for key in resDict:
        print(("{0}: {1}").format(key.title(), str(getStockAmount(resDict, key))))
    print()