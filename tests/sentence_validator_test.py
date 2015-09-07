__author__ = 'kskrishnasangeeth'

import unittest
from algopy.sentence_validator import validator

class SentenceValidatorTestCase(unittest.TestCase):
    def test_fullstop(self):
        truth = validator("This is a test statement.A proper statement.")
        self.assertEquals(truth,True)


