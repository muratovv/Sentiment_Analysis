#!/usr/bin/env python3
__author__ = 'muratov'

import pymorphy2
import re

def normalizeText(text):
    """
    :param text: Исходный текст
    :return: Нормализованный набор слов из текста.
    """
    morph = pymorphy2.MorphAnalyzer()
    normalizedList = list()
    for word in text.split():
        word = re.sub("\W", "", word)
        word = morph.parse(word)[0].normal_form
        normalizedList.append(word)
    return " ".join(normalizedList)

