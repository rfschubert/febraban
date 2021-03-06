from unittest.case import TestCase
from febraban.cnab240.row import numeric, alphaNumeric
from febraban.cnab240.v83.file.header import Header
from febraban.cnab240.v83.file.trailer import Trailer


class FileTest(TestCase):

    def testHeaderLengh(self):
        string = Header().toString()
        self.assertEqual(len(string), 240)

    def testTrailorLengh(self):
        string = Trailer().toString()
        self.assertEqual(len(string), 240)

    def testHeaderDefaultValues(self):
        elements = Header().elements
        self.assertEqual(elements[4].value(), "081")

    def testTrailerDefaultValues(self):
        elements = Trailer().elements
        self.assertEqual(elements[1].value(), "9999")
        self.assertEqual(elements[2].value(), "9")

    def testHeaderPositions(self):
        elements = Header().elements
        currentPositions = [(e.numberOfCharacters, e.charactersType) for e in elements]
        rightPositions = [
            (3,  numeric),
            (4,  numeric),
            (1,  numeric),
            (6,  alphaNumeric),
            (3,  numeric),
            (1,  numeric),
            (14, numeric),
            (20, alphaNumeric),
            (5,  numeric),
            (1,  alphaNumeric),
            (12, numeric),
            (1,  alphaNumeric),
            (1,  numeric),
            (30, alphaNumeric),
            (30, alphaNumeric),
            (10, alphaNumeric),
            (1,  numeric),
            (8,  numeric),
            (6,  numeric),
            (9,  numeric),
            (5,  numeric),
            (69, alphaNumeric)
        ]
        self.assertEquals(rightPositions, currentPositions)

    def testTrailerPositions(self):
        elements = Trailer().elements
        currentPositions = [(e.numberOfCharacters, e.charactersType) for e in elements]
        rightPositions = [
            (3,   numeric),
            (4,   numeric),
            (1,   numeric),
            (9,   alphaNumeric),
            (6,   numeric),
            (6,   numeric),
            (211, alphaNumeric)
        ]
        self.assertEquals(rightPositions, currentPositions)