#!/usr/bin/env python3
__author__ = 'muratov'

import xml.etree.ElementTree as ET
import os
import logging

import projectConfigs


projectConfigs.CONSTS["loggin_file"] = "{0}.log".format(os.path.basename(__file__))
projectConfigs.setLogConfig()


class XmlParser:
    """
    Класс для преобразования xml -> dict
    """

    def __init__(self, pathToDirectory, needAttributes, addPath=False):
        """
        :param pathToDirectory: Путь к папке с xml-файлами. Вложенные папки поддерживаются;
        :param needAttributes: Доставаемые атрибуты;
        :param addPath: Добалять ли путь до файла в конечный словарь. XmlParse["file"]
        :return:
        """
        self.needAttributes = needAttributes
        self.iter = None
        self.addPath = addPath
        if os.path.isdir(pathToDirectory):
            self.directory = pathToDirectory
        else:
            raise EnvironmentError("Directory {0} not exist".format(pathToDirectory))

    def __iter__(self):
        self.iter = iter(self.__parseFolder())
        return self.iter

    def __next__(self):
        return next(self.iter)

    def __parseNextFile(self, path):
        parsed = dict()
        root = ET.parse(path).getroot()
        for child in root:
            if child.tag in self.needAttributes:
                parsed[child.tag] = child.text.strip()
        if self.addPath:
            parsed["file"] = path
        return parsed


    def __parseFolder(self):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                filePath = os.path.join(root, file)
                if os.path.splitext(filePath)[1] == ".xml":
                    result = self.__parseNextFile(filePath)
                    logging.info("file {0} parsed".format(filePath))
                    yield result


if __name__ == '__main__':
    print(projectConfigs.CONSTS["blog_collection_path"])
    p = XmlParser(projectConfigs.CONSTS["blog_collection_path"], ['real_object', 'score-2', 'text'])
    p = iter(p)
    i = 0
    while i < 3:
        print(next(p))
        i += 1