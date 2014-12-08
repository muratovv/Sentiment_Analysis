#!/usr/bin/env python3
__author__ = 'muratov'

import random

from SAMethods.Abstract import AbstractMethod


class RandomMethod(AbstractMethod):
    def getReaction(self, text):
        return random.choice([1, 2])

    def setTrainingSamples(self, samples):
        pass



if __name__ == '__main__':
    r = RandomMethod()
    print(r.getReaction("123"))