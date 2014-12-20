#!/usr/bin/env python3
__author__ = 'muratov'

from SAMethods.Abstract import AbstractMethod
from PrepareData.Normalize import normalizeText
import ProjectConfigs as config

sentimentDict = dict()


def initDictionary(path):
    with open(path, "r") as file:
        for line in file.readlines():
            line = line.split()
            sentimentDict[line[0]] = float(line[1])


initDictionary(config.CONSTS["dict"])


class DictionaryMethod(AbstractMethod):
    def setTrainingSamples(self, samples):
        pass

    def predict(self, text):
        sum_ = 0.0
        text = normalizeText(text)
        for keyWord in sentimentDict.keys():
            if keyWord in text:
                sum_ += sentimentDict[keyWord]
        if sum_ >= 0:
            return 2
        else:
            return 1


if __name__ == '__main__':
    d = DictionaryMethod()
    print(d.predict("адекватное"))
