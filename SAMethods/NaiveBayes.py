#!/usr/bin/env python3
__author__ = 'muratov'
from collections import defaultdict

from PrepareData.Normalize import normalizeText

from SAMethods.Abstract import AbstractMethod


class NaiveBayes(AbstractMethod):
    def __init__(self):
        self.sampleDict = {1: defaultdict(int), 2: defaultdict(int)}  # встречаемость слова в классе
        self.vocabulary = 0  # количество уникальных слов
        self.classWords = {1: 0, 2: 0}  # количество слов в классе.
        self.aprioriProbability = {1: 0, 2: 0}  # априорная вероятность

    def setTrainingSamples(self, samples):
        testQuantity = 0
        for sample in samples:
            text = normalizeText(sample[0]).split()
            for word in text:
                self.sampleDict[sample[1]][word] += 1
                self.classWords[sample[1]] += 1
            testQuantity += 1
            self.aprioriProbability[sample[1]] += 1
        self.vocabulary = len(set(self.sampleDict[1]) | set(self.sampleDict[2]))
        self.aprioriProbability[1] /= testQuantity
        self.aprioriProbability[2] /= testQuantity

    def predict(self, text):
        probs = {1: self.aprioriProbability[1], 2: self.aprioriProbability[2]}  # вероятности нахождения в классах key
        dDict = defaultdict(int)  # bag of words
        for word in normalizeText(text).split():
            dDict[word] += 1
        for unicWord in dDict.keys():
            probs[1] *= self.evaluateProbabilityInClass(unicWord, 1) ** dDict[unicWord]
            probs[2] *= self.evaluateProbabilityInClass(unicWord, 2) ** dDict[unicWord]
        if probs[1] > probs[2]:
            return 1
        else:
            return 2

    def evaluateProbabilityInClass(self, word, cls):
        return (1 + self.sampleDict[cls][word]) / (self.classWords[cls] + self.vocabulary)


if __name__ == '__main__':
    nb = NaiveBayes()
    nb.setTrainingSamples([("китай пекин китай", 1), ("китай китай шанхай", 1), ("китай макао", 1), ("токио япония китай", 2), ])
    print(nb.predict("китай китай китай токио япония"))
