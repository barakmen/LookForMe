import face_recognition
import os
from shutil import copy
import sys
import shutil

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
        
def findAndExport(currentPersonPath, folderToSearchPath, destDirPath):
    if os.path.exists(destDirPath):
        for the_file in os.listdir(destDirPath):
            file_path = os.path.join(destDirPath, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
    return getPicsOfPersonInFolder(currentPersonPath,folderToSearchPath, lambda picPath: exportFile(picPath, destDirPath))

    