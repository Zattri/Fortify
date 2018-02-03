# Gets the stock amount of a resource
def getStockAmount(resDict, dictKey):
    return resDict[dictKey][0]

# Gets the gathering amount of a resource
def getGatherAmount(resDict, dictKey):
    return resDict[dictKey][1]

# Gather a resource of any type, increasing the stock amount of that resource by the gather amount
def updateStock(resDict, dictKey):
    dictKey = dictKey.lower()
    resDict.update({dictKey: [(resDict[dictKey][0] + resDict[dictKey][1]), resDict[dictKey][1]]})
    return resDict

# Gather every resource, increasing the stock amount by the gather amount
def updateAllStock(resDict):
    for key in resDict:
        resDict.update({key: [(resDict[key][0] + resDict[key][1]), resDict[key][1]]})
    return resDict