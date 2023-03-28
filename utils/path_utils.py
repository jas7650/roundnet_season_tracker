import os


def joinPath(path1, path2):
    return os.path.join(path1, path2)


def isFile(file):
    return os.path.isfile(file)


def listDir(path):
    return os.listdir(path)


def pathExists(path):
    return os.path.exists(path)


def splitText(text):
    return os.path.splitext(text)


def getBaseName(file):
    return os.path.basename(file)


def getCurrentLocation():
    return os.getcwd()