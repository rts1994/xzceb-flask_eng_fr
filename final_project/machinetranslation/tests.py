import unittest
from translator import englishToFrench, frenchToEnglish

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        self.assertNotEqual(englishToFrench('None'), '')
        self.assertNotEqual(englishToFrench(0),0)

    def test2(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        self.assertNotEqual(frenchToEnglish('None'), '')
        self.assertNotEqual(frenchToEnglish(0),0)

unittest.main()