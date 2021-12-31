import textwrap as tr


class Entity:

    def __init__(self, *args):

        self.name = args[0]
        self.description = args[1]

    def test(self):
        print(self.name)
        text = tr.fill(self.description)
        print(text + "\n\n")

    def __eq__(self, other):
        return self.name == other.name
        