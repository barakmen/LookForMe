import face_recognition

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
    unknown_face_encoding = unknown_face_encoding_arr[0]
    
    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

    return results[0] == True

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
    

    