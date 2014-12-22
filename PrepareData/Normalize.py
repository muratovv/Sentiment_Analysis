#!/usr/bin/env python3
__author__ = 'muratov'

import re
import os

import pymorphy2

from PrepareData.StructureDataBuilder import BuildStructure
import ProjectConfigs
def normalizeText(text):
    """
    :param text: Исходный текст
    :return: Нормализованный набор слов из текста.
    """
    morph = pymorphy2.MorphAnalyzer()
    normalizedList = list()
    for word in text.split():
        word = re.sub("\W", "", word)
        word = word.lower()
        word = morph.parse(word)[0].normal_form
        normalizedList.append(word)
    return " ".join(normalizedList)


def normalizeTextInDir(sourseDir, destDir):
    bs = BuildStructure(destDir, sourseDir)
    for doc in bs:
        print(doc["file"])
        bs.writeFile(doc["score-2"], os.path.basename(doc["file"]), normalizeText(doc["text"]))


if __name__ == '__main__':
    soursePath = os.path.join(ProjectConfigs.CONSTS["row_data"], "blog_train_final")
    destPath = os.path.join(ProjectConfigs.CONSTS["structured_data"], "normalize_blog_train_final")
    normalizeTextInDir(soursePath, destPath)
