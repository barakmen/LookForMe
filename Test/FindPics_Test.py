import unittest
import sys
sys.path.insert(0, '../')
import lookforme
import os

class TestStringMethods(unittest.TestCase):
    '''
    def test_findpics(self):
        resourceFolder = 'TestResources'
        #callback is optional!!!
        pics = lookforme.getPicsOfPersonInFolder(resourceFolder + '/ubama.jpg',resourceFolder, lambda picPath: print('Find : ' + picPath))
        self.assertTrue(len(pics) == 2)
    '''
    def test_copyfiles(self):
        folderToSearch = 'TestResources'
        resultFolder = 'resultFolder'
        pics = lookforme.findAndExport(folderToSearch + '/ubama.jpg',folderToSearch, resultFolder)        
        self.assertTrue(os.path.isdir(resultFolder))

if __name__ == '__main__':
    unittest.main()