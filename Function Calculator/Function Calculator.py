class Equasion:
    def __init__(self, eq: str):

        # Equasion
        if not eq: raise ValueError("eq needs to be a function")
        self.eq = eq

        # terms in the equasion
        self.terms = [[]]  # each list in the terms list is a seperate equality (unless specified that it is not)
        self.find_terms()

        # the variables
        self.vars = []
        self.find_vars()

    def find_terms(self):
        previous_i = 0
        for i, char in enumerate(self.eq):
            if char in ['/', '*', '-', '+', '^']:
                self.terms[-1].append(self.eq[previous_i:i])
                previous_i = i
            elif char in ['(', '[', '{']:
                self.terms[-1].append(self.eq[previous_i:i])
                self.terms[-1].append(self.eq[i:self.find_corr(i)])
                previous_i = self.find_corr(i)
            if char == '=':
                self.terms[-1].append(self.eq[previous_i:i])
                previous_i = i+1
                self.terms.append([])
        self.terms[-1].append(self.eq[previous_i:i+1])

    def find_corr(self, i):
        """
        finds the corisponding bracket at the start index
        :param i: the starting index which this function will start checking self.eq on
        :return: the index that the corrisponding bracket has
        """
        corisponding = {'(': ')', '[': ']', '{': '}'}
        amount = 1
        while amount > 0 or i != len(self.eq):
            if self.eq[i]:
                amount += 1
            elif corisponding[self.eq[i]]:
                amount -= 1
            i += 1
        return i

    def find_vars(self):
        """
        find the variables in the eq
        """
        for char in self.eq:
            if char.isalpha():
                self.vars.append(char)

    def POEs(self):
        corr = {
            '+': '-', 
            '-': '+',
            '*': '/',
            '/': '*'
        }


def read_file():
    """
    reads a file and that file is the input
    """
    with open('Equasions.txt') as f:
        file = f.read()
    equations = []
    break_line = True
    previous = 0
    for i, char in enumerate(file):
        if char == '\n' and break_line:
            equations.append(file[previous:i].replace('\n', ''))
            previous = i
        elif char == '\n' and not break_line:
            break_line = True
        elif char == "/":
            break_line = False
        if i+1 == len(file):
            equations.append(file[previous:i+1].replace('\n', '').replace('/', '').replace(' ', ''))
    return equations


def main():
    print('file: ', read_file())
    eq = Equasion('x=2(15)')
    print(eq.terms)
    print(eq.vars)


if __name__ == "__main__":
    main()
