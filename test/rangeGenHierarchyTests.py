import unittest
import src.rangeGenHierarchy as RGH


class ExtendedTestCase(unittest.TestCase):

  def assertRaisesWithMessage(self, msg, func, *args, **kwargs):
    try:
      func(*args, **kwargs)
      self.assertFail()
    except Exception as inst:
      self.assertEqual(inst.message, msg)


#  test_ prefix for methods is needed in python unittest
class RangeGenHierarchyMethods(ExtendedTestCase):

    def test_rangeGenAgeMinGreaterMax(self):
        self.assertRaisesWithMessage('Range invalid. Min greater than max.',
                                     RGH.RangeGenHierarchy,
                                     'age', 10, -5)


    def test_rangeGenAgeMinEqualsMax(self):
        self.assertRaisesWithMessage('Range invalid. Min equals max.',
                                     RGH.RangeGenHierarchy,
                                     'age', 10, 10)


    def test_rangeGenAgeGenToNegRange(self):
        rgh = RGH.RangeGenHierarchy('age', 10, 90)
        self.assertRaisesWithMessage('Cannot generalize to negative range.',
                                     rgh.getCostOfRange,
                                     40, 30)


    def test_rangeGenAgeGenLowOutside(self):
        rgh = RGH.RangeGenHierarchy('age', 10, 90)
        self.assertRaisesWithMessage('Low parameter less than range minimum.',
                                     rgh.getCostOfRange,
                                     5, 30)


    def test_rangeGenAgeGenHighOutside(self):
        rgh = RGH.RangeGenHierarchy('age', 10, 90)
        self.assertRaisesWithMessage('High parameter greater than range maximum.',
                                     rgh.getCostOfRange,
                                     50, 100)


    def test_rangeGenAgeGenValid(self):
        rgh = RGH.RangeGenHierarchy('age', 10, 90)
        self.assertEqual(rgh.getCostOfRange(30, 50), 0.25)


if __name__ == '__main__':
    unittest.main()