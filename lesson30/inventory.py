from rock import Rock


class Inventory:
    def __init__(self):
        self.rocks = []

    def add_rock(self, rock):
        self.rocks.append(rock)

    def remove_rock(self, rock):
        self.rocks.remove(rock)

    def list_inventory(self):
        return [r.get_info() for r in self.rocks]

    def filterByname(self, name):
        return [r for r in self.rocks if r.name == name]

    def filterBycolor(self, color):
        return [r for r in self.rocks if r.color == color]
