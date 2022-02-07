class Candidate:
    def __init__(self, name, number, group):
        self.name = name
        self.number = number
        self.group = group

    def __repr__(self) -> str:
        return f'i\'m {self.name} the number {self.number} of the group {self.group}'


class Vote:
    candidates = []
    def __init__(self):
        self.candidates.append('Eric Zemour')
        self.candidates.append('Jean-luc Melenchon')
        self.candidates.append('Marine Lepen')
        print(self.candidates)

    def vote():
        pass

v = Vote()
