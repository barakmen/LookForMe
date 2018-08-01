import face_recognition

def isSamePerson(currentPersonPath, otherPath):

    picture_of_me = face_recognition.load_image_file(currentPersonPath)
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    # my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

    unknown_picture = face_recognition.load_image_file(otherPath)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

    # Now we can see the two face encodings are of the same person with `compare_faces`!

    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

    return results[0] == True

def getPicsOfPersonInFolder(currentPersonPath, dirPath):
    import os
    samePerson = []
    for subdir, dirs, files in os.walk(dirPath):
        for file in files:
            filepath = subdir + os.sep + file
            if(isSamePerson(currentPersonPath, filepath)):
                samePerson.append(os.path.abspath(filepath))
    return samePerson
    

