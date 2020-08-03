import unittest
from planetRegister import planetRegister

class NamesTestCase(unittest.TestCase):
    """Tests for 'planetRegister_functions.py'"""

    def test_planet_register(self):
        """Do names like Agripinaa of Obscurus work?"""
        location_input = planetRegister("Agripinaa", "Obscurus")
        self.assertEqual(location_input, "Planet Agripinaa is located at segmentum Obscurus.")

unittest.main()