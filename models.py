class Lfa:

    def __init__(self):
        self.lfas = [{'team': 'Adrian', 'password': 'one'},
                     {'team': 'Angela', 'password': 'two'},
                     {'team': 'Arnold', 'password': 'three'},
                     {'team': 'David', 'password': 'four'},
                     {'team': 'Deo', 'password': 'five'},
                     {'team': 'Hadijah', 'password': 'six'},
                     {'team': 'Phiona', 'password': 'seven'},
                     {'team': 'Shakira', 'password': 'eight'}]
        self.bootcampers = {}
        self.bcs = []

    def login(self, team, password):
        for group in self.lfas:
            if group['team'] == team and group['password'] == password:
                for bc in self.bootcampers:
                    if bc['team'] == team:
                        self.bcs[bc['username']] == bc
        return self.bcs

    def award(self):
        value = input('Value: ')
        point = int(input('point ':))
        username = input('Username: ')
        points = [-2, -1, 0, 1, 2]
        award = None
        for p in points:
            if p == point:
                award = p
                bc = self.bcs[username]
                bc['scores'][value] = award
                return "Award successfull."
        else:
            return 'Something went wrong.'