#!/usr/bin/env python3
__author__ = 'muratov'

from abc import ABCMeta, abstractclassmethod


class AbstractMethod(metaclass=ABCMeta):
    @abstractclassmethod
    def setTrainingSamples(self, samples):
        """
        :param Set: samples - iterable with (text, answer)
        :return:
        """
        pass

    @abstractclassmethod
    def getReaction(self, text):
        pass

    def __filter(self):
        pass