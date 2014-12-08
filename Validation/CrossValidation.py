#!/usr/bin/env python3
__author__ = 'muratov'
from PrepareData.StructureDataBuilder import BuildStructure
import projectConfigs as config


class CVSampleCreator:
    def __init__(self, rowDataPath, parts):
        self.path = rowDataPath
        self.k = parts

    def getParts(self):
        streammer = BuildStructure(None, self.path)
        currentPart = 0
        partList = [[] for part in range(self.k)]
        for obj in streammer:
            partList[currentPart].append(obj["file"])
            currentPart = (currentPart + 1) % self.k
        return partList


if __name__ == '__main__':
    sampleCreator = CVSampleCreator(config.CONSTS["blog_collection_path"], 3)
    partNum = 0
    for part in sampleCreator.getParts():
        print("part {0} have {1} elements".format(partNum, len(part)))

