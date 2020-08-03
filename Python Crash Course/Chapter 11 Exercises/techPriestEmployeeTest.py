import unittest
from techPriestEmployee import TechPriestEmployee

class TestTPE(unittest.TestCase):
    """Test for the class TechPriestEmployee"""

    def setUp(self):
        """Creates the print template for employee raises"""
        self.helios = TechPriestEmployee("Helios","Archmagos")

    def thrones_raise_test(self):
        """Tests to see that the default value function of 'give_raise' works"""
        self.helios.give_raise()
        self.assertIn(15000, self.thrones_salary)

    def custom_thrones_raise_test(self):
        """"""
        self.helios.give_raise(8000)
        self.assertIn(18000, self.thrones_salary)

unittest.main()