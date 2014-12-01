#!/usr/bin/env python3
__author__ = 'muratov'
import logging
import os

# TODO configure log instance

CONSTS = dict()
# Loggin Consts
CONSTS["loggin_format"] = '%(filename)s[LINE:%(lineno)d]# %(levelname)-1s [%(asctime)s]  %(message)s'
CONSTS["loggin_file"] = "logs"
CONSTS["base_path"] = os.path.dirname(__file__)
CONSTS["loggin_level"] = logging.DEBUG
#

# Path consts
CONSTS["blog_collection_path"] = "RowData/blog_train_final"
CONSTS["structured_data_path"] = "StructuredData/blog_train_final"
#

def setCollectionPath():
    CONSTS["blog_collection_path"] = os.path.join(CONSTS["base_path"], CONSTS["blog_collection_path"])
    CONSTS["structured_data_path"] = os.path.join(CONSTS["base_path"], CONSTS["structured_data_path"])


def setLogConfig():
    if CONSTS["loggin_file"] is None:
        logging.basicConfig(format=CONSTS["loggin_format"], level=CONSTS["loggin_level"])
    else:
        path = os.path.join(CONSTS["base_path"], CONSTS["loggin_file"])
        logging.basicConfig(format=CONSTS["loggin_format"], level=CONSTS["loggin_level"], filename=path)



def defaultConfigs():
    setLogConfig()
    setCollectionPath()



if __name__ == '__main__':
    logging.debug("Отладочное сообщение")
    logging.info("Информационное сообщение")
    logging.warning("Предупреждение")
    logging.error("Ошибка")
    logging.critical("Critical error")