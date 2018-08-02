import face_recognition
import os
from shutil import copy
import sys
import shutil
import calendar
import time
import glob

def isSamePerson(currentPersonPath, otherPath):

    picture_of_me = face_recognition.load_image_file(currentPersonPath)
    my_face_encoding_arr = face_recognition.face_encodings(picture_of_me)
    if(len(my_face_encoding_arr) <= 0):
        return False
    my_face_encoding = my_face_encoding_arr[0]

    unknown_picture = face_recognition.load_image_file(otherPath)
    unknown_face_encoding_arr = face_recognition.face_encodings(unknown_picture)
    if(len(unknown_face_encoding_arr) <= 0):
        return False
    
    for i in range(len(unknown_face_encoding_arr)):
        unknown_face_encoding = unknown_face_encoding_arr[i]
        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
        if(results[0] == True):
            return True
    return False

def getPicsOfPersonInFolder(currentPersonPath, dirPath, callback = None):
    import os
    samePerson = []
    for subdir, dirs, files in os.walk(dirPath):
        for file in files:
            filepath = subdir + os.sep + file
            if(isSamePerson(currentPersonPath, filepath)):
                if(callback):
                    callback(filepath)
                samePerson.append(os.path.abspath(filepath))
    return samePerson


def exportFile(pathToFile, destDir):
    if not os.path.exists(destDir):
        os.makedirs(destDir)
    copy(pathToFile, destDir)


def deleteFilesFromDir(dirPath):
    if os.path.exists(dirPath):
        for the_file in os.listdir(dirPath):
            file_path = os.path.join(dirPath, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

def moveFilesToDir(fromDir, toDir):
    
    ts = calendar.timegm(time.gmtime())
    if not os.path.exists(toDir):
        os.makedirs(toDir)

    newdest = toDir + '/' + str(ts)
    if not os.path.exists(newdest):
        os.makedirs(newdest)

    for file in glob.glob(fromDir+"\\*"):
        shutil.copy2(file, newdest);
    


def findAndExport(currentPersonPath, folderToSearchPath, destDirPath):
    moveFilesToDir(destDirPath, 'trash')
    deleteFilesFromDir(destDirPath)
    return getPicsOfPersonInFolder(currentPersonPath,folderToSearchPath, lambda picPath: exportFile(picPath, destDirPath))


def OpenTrashFolder():
    toDir = 'trash'
    if not os.path.exists(toDir):
        os.makedirs(toDir)
    os.startfile(toDir)

