import unittest 
from inventory import TestInventory

suite = unittest.TestLoader().loadTestsFromTestCase(TestInventory)
unittest.TextTestRunner().run(suite)
                                        