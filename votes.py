class Candidate:
    def __init__(self, name, number, group):
        self.name = name
        self.number = number
        self.group = group

    def __repr__(self) -> str:
        return f'i\'m {self.name} the number {self.number} of the group {self.group}'


class Vote:
    candidates = []
    def __init__(self, candidates):
        self.candidates = candidates

    def vote():
        pass

candidates = []
candidates.append(Candidate('Eric zemour', 1, 'republicain'))
candidates.append(Candidate('Jean-luc Melenchon', 1, 'Droite'))
candidates.append(Candidate('Marine Lepen', 1, 'Gauche'))

