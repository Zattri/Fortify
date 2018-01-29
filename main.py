import pygame
import resource
import building
import index


def main():
    # dict(key<resourceType>: [stockAmount, gatherAmount])
    resourceDict = {"stone": [10, 5], "wood": [10, 5], "fish": [0, 5]}
    myBuildings = index.buildingIndex
    upgradeIndex = index.upgradeIndex # Make const

    resourceDict = resource.updateStock(resourceDict, "stone")
    resourceDict = resource.updateAllStock(resourceDict)

    resource.printStockAmount(resourceDict)
    building.printBuildings(myBuildings)

    returnTuple = building.upgradeBuilding(0, myBuildings, upgradeIndex, resourceDict)
    resourceDict = returnTuple[0]
    myBuildings = returnTuple[1]

    resource.printStockAmount(resourceDict)
    building.printBuildings(myBuildings)

    returnTuple = building.upgradeBuilding(0, myBuildings, upgradeIndex, resourceDict)
    resourceDict = returnTuple[0]
    myBuildings = returnTuple[1]

    resource.printStockAmount(resourceDict)
    building.printBuildings(myBuildings)

main()