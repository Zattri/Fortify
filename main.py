import pygame
import resource


def main():
    # dict(key<resourceType>: [stockAmount, gatherAmount])
    resourceDict = {"stone": [0, 5], "wood": [0, 5], "fish": [0, 5]}
    print(resourceDict)
    resourceDict = resource.updateStock(resourceDict, "stone")
    print(resourceDict)
    resourceDict = resource.updateAllStock(resourceDict)
    print(resourceDict)
    resourceDict = resource.increaseGatherAmount(resourceDict, "stone", 2)
    print(resourceDict)
    resourceDict = resource.updateAllStock(resourceDict)
    print(resourceDict)

main()