#!/usr/bin/env python3
__author__ = 'muratov'

import os
import logging

from PrepareData.XmlCleanUp import XmlParser
import projectConfigs


projectConfigs.CONSTS["loggin_file"] = "{0}.log".format(os.path.basename(__file__))
projectConfigs.defaultConfigs()


class BuildStructure:
    def __init__(self, destPath, xmlPath):
        self.destPath = destPath
        self.xmlPath = xmlPath
        self.__createDir("1")
        self.__createDir("2")
        self.__strucure()


    def __createDir(self, folder):
        path = os.path.join(self.destPath, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            logging.info("created {0}".format(path))

    def writeFile(self, dest, text):
        with open(dest, "w") as file:
            file.write(text)
            logging.info("write {0}".format(dest))

    def __strucure(self):
        parser = XmlParser(self.xmlPath, ["score-2", "text"], True)
        for file in parser:
            path = os.path.join(self.destPath, file["score-2"], os.path.basename(file["file"]))
            self.writeFile(path, file["text"])
            logging.info("write {0}".format(path))


if __name__ == '__main__':
    bs = BuildStructure(projectConfigs.CONSTS["structured_data_path"],
                        projectConfigs.CONSTS["blog_collection_path"])
