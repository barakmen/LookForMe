import unittest
import sys
sys.path.insert(0, '../')
import lookforme


class TestStringMethods(unittest.TestCase):

    def test_findpics(self):
        resourceFolder = 'TestResources'
        
        #callback is optional!!!
        pics = lookforme.getPicsOfPersonInFolder(resourceFolder + '/haim.jpg',resourceFolder, lambda picPath: print('Find : ' + picPath))
        self.assertTrue(len(pics) == 2)

if __name__ == '__main__':
    unittest.main()