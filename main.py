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


    output.stockAmount(resourceDict)
    output.buildingList(myBuildings)
    output.techTree(techTree)

    resourceDict, myBuildings, techTree = building.upgradeBuilding(0, myBuildings, upgradeIndex, techTree, resourceDict)

    output.stockAmount(resourceDict)
    output.buildingList(myBuildings)
    output.techTree(techTree)

    resourceDict, myBuildings, techTree = building.upgradeBuilding(1, myBuildings, upgradeIndex, techTree, resourceDict)
    resourceDict, myBuildings, techTree = building.upgradeBuilding(2, myBuildings, upgradeIndex, techTree, resourceDict)
    resourceDict, myBuildings, techTree = building.upgradeBuilding(3, myBuildings, upgradeIndex, techTree, resourceDict)
    resourceDict, myBuildings, techTree = building.upgradeBuilding(4, myBuildings, upgradeIndex, techTree, resourceDict)
    resourceDict, myBuildings, techTree = building.upgradeBuilding(5, myBuildings, upgradeIndex, techTree, resourceDict)

    output.stockAmount(resourceDict)
    output.buildingList(myBuildings)
    output.techTree(techTree)

main()