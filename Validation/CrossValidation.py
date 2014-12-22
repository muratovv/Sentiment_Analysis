#!/usr/bin/env python3
__author__ = 'muratov'
from PrepareData.StructureDataBuilder import BuildStructure
import ProjectConfigs as config


class CVSampleExtractor:
    def __init__(self, rowDataPath, parts):
        self.path = rowDataPath
        self.k = parts

    def getParts(self):
        streammer = BuildStructure(None, self.path)
        currentPart = 0
        partList = [[] for part in range(self.k)]
        for obj in streammer:
            partList[currentPart].append((obj["text"], int(obj["score-2"])))
            currentPart = (currentPart + 1) % self.k
        return partList


class CVTestMethod:
    def __init__(self, sampleDir, itersCounter):
        extractor = CVSampleExtractor(sampleDir, itersCounter)
        self.data = extractor.getParts()

    def runTest(self, methodClass):

        curtIter = 0
        markSum = 0.0
        while curtIter < len(self.data):

            print("Testing part {0}".format(curtIter))

            method = methodClass()
            samples = []
            for trainSet in self.data[:curtIter] + self.data[curtIter + 1:]:
                for example in trainSet:
                    samples.append(example)
            method.setTrainingSamples(samples)
            markSum += self.testReaction(method, self.data[curtIter])
            curtIter += 1
        return markSum / len(self.data)

    def testReaction(self, method, testPart):
        markSum = 0
        for request in testPart:
            answer = method.predict(request[0])
            if answer == request[1]:
                markSum += 1
        return markSum / len(testPart)


from SAMethods.Random import RandomMethod
from SAMethods.Dictionary import DictionaryMethod
from SAMethods.NaiveBayes import NaiveBayes

if __name__ == '__main__':
    sampletester = CVTestMethod(config.CONSTS["blog_collection_path"], 10)
    print("Random - {0}".format(sampletester.runTest(RandomMethod)))
    print("Naive Bayes - {0}".format(sampletester.runTest(NaiveBayes)))
    print("Dict - {0}".format(sampletester.runTest(DictionaryMethod)))

