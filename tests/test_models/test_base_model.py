#!/usr/bin/python3

""" Unit testing """

import unittest
import models
from datetime import datetime

class TestBaseModel(unittest.TestCase):
	def test__str__(self):
		self.assertIsNot(clsname, None, "A string is required")
		self.assertIsNot(self.id, None, " A string is required")
		self.assertIsNot(self.__dict__, None, "A string is required")

if __name__ == '__main__':
	unittest.main()
