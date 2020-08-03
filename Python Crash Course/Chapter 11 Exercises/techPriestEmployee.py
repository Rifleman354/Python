class TechPriestEmployee():
    """Manages tech priest data and salary"""

    def __init__(self, name, rank, thrones_salary):
        """Initialize attributes in the tech priest database"""
        self.name = name
        self.rank = rank
        self.thrones_salary = 10000

    def give_raise(self, thrones_raise=5000):
        """Specifies the raise amount of thrones a tech priest gets due to promotion"""
        thrones_salary += thrones_raise