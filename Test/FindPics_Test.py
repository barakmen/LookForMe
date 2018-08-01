import unittest
import sys
sys.path.insert(0, '../')
import lookforme


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        resourceFolder = 'TestResources'
        pics = lookforme.getPicsOfPersonInFolder(resourceFolder + '/ubama.jpg',resourceFolder)
        self.assertTrue(len(pics) == 2)



if __name__ == '__main__':
    unittest.main()