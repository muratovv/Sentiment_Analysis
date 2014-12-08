#!/usr/bin/env python3
__author__ = 'muratov'

import os
import logging

from PrepareData.XmlCleanUp import XmlParser
import ProjectConfigs


ProjectConfigs.CONSTS["loggin_file"] = "{0}.log".format(os.path.basename(__file__))
ProjectConfigs.defaultConfigs()


class BuildStructure:
    #TODO переназвать класс.
    """
    Класс для потоковой обработки входных файлов.
    """

    def __init__(self, destPath, xmlDir):
        """
        :param destPath: Папка в которой будет хранится выборка.
        :param xmlDir: Папка с исходными текстами.
        :return:
        """
        self.destPath = destPath
        self.xmlPath = xmlDir

    def createContexDir(self, folder):
        path = os.path.join(self.destPath, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            logging.info("created {0}".format(path))

    def writeFile(self, dest, fileName, text):
        """
        :param dest: относительный путь.
        :param text: записываемый текст.
        :return:
        """
        path = os.path.join(self.destPath, dest, fileName)
        with open(path, "w") as file:
            file.write(text)
            logging.info("write {0}".format(path))

    def __strucure(self):
        parser = XmlParser(self.xmlPath, ["score-2", "text"], True)
        for file in parser:
            path = os.path.join(self.destPath, file["score-2"], os.path.basename(file["file"]))
            self.writeFile(path, file["text"])
            logging.info("write {0}".format(path))

    def __iter__(self):
        self.it = XmlParser(self.xmlPath, ["score-2", "text"], True)
        return iter(self.it)

    def __next__(self):
        res = next(self.it)
        return res


if __name__ == '__main__':
    bs = BuildStructure(ProjectConfigs.CONSTS["structured_data_path"],
                        ProjectConfigs.CONSTS["blog_collection_path"])
    i = 0

    for file in bs:
        print(file)
        i += 1
        if i == 3:
            break


