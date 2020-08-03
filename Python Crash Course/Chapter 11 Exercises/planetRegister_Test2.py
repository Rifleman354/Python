import unittest
from planetRegister2 import planetRegister2

class NamesTestCase(unittest.TestCase):
    """Tests for 'planetRegister_functions.py'"""

    def test_planet_register(self):
        """Do names like Agripinaa of Obscurus work?"""
        location_input = planetRegister2("Agripinaa", "Obscurus", 2000000)
        self.assertEqual(location_input, "Planet Agripinaa is located in segmentum Obscurus; population: 2000000")

unittest.main()