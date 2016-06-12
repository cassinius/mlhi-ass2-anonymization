import unittest
import src.catGenHierarchy as CGH


#  test_ prefix for methods is needed in python unittest
class CatGenHierarchyMethods(unittest.TestCase):

    def test_catGenSexLevels(self):
        cgh = CGH.CatGenHierarchy('sex', '../data/gen_hierarchies/SexGH.json')
        self.assertEqual(cgh.getNrLevels(), 1)


    def test_catGenCountryLevels(self):
        cgh = CGH.CatGenHierarchy('native-country', '../data/gen_hierarchies/NativeCountryGH.json')
        self.assertEqual(cgh.getNrLevels(), 3)


    def test_catGenSexGetGenOfMale(self):
        cgh = CGH.CatGenHierarchy('sex', '../data/gen_hierarchies/SexGH.json')
        self.assertEqual(cgh.getGeneralizationOf('Male'), 'all')


    def test_catGenCountryGetGenOfCambodia(self):
        cgh = CGH.CatGenHierarchy('native-country', '../data/gen_hierarchies/NativeCountryGH.json')
        self.assertEqual(cgh.getGeneralizationOf('Cambodia'), 'East-Asia')


    def test_catGenCountryGetGenOfEastAsia(self):
        cgh = CGH.CatGenHierarchy('native-country', '../data/gen_hierarchies/NativeCountryGH.json')
        self.assertEqual(cgh.getGeneralizationOf('East-Asia'), 'Asia')


    def test_catGenCountryGetGenOfAsia(self):
        cgh = CGH.CatGenHierarchy('native-country', '../data/gen_hierarchies/NativeCountryGH.json')
        self.assertEqual(cgh.getGeneralizationOf('Asia'), 'all')




if __name__ == '__main__':
    unittest.main()