import pygame
import resource
import building
import index
import output


def main():
    # dict(key<resourceType>: [stockAmount, gatherAmount])
    resourceDict = index.resourceDictionary
    myBuildings = index.buildingIndex
    upgradeIndex = index.upgradeIndex
    techTree = index.techIndex

    resourceDict = resource.updateStock(resourceDict, "stone")
    resourceDict = resource.updateAllStock(resourceDict)

    output.stockAmount(resourceDict)
    output.buildingList(myBuildings)
    output.techTree(techTree)

    resourceDict, myBuildings, techTree = building.upgradeBuilding(0, myBuildings, upgradeIndex, techTree, resourceDict)

    output.stockAmount(resourceDict)
    output.buildingList(myBuildings)
    output.techTree(techTree)

    resourceDict, myBuildings, techTree = building.upgradeBuilding(0, myBuildings, upgradeIndex, techTree, resourceDict)

    output.stockAmount(resourceDict)
    output.buildingList(myBuildings)
    output.techTree(techTree)

    resourceDict = resource.updateStock(resourceDict, "wood")
    output.stockAmount(resourceDict)

main()