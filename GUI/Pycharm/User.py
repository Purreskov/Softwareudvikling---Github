class User_Patients:
    def __init__(self, cpr, weight, fev1, GOLD, MRC):

        self.cpr = cpr
        self.weight = weight
        self.fev1 = fev1
        self.GOLD = GOLD
        self.MRC = MRC

class User_Person:
    def __init__(self, name, age, telephone, cpr):

        self.cpr = cpr
        self.name = name
        self.telephone = telephone
        self.age = age