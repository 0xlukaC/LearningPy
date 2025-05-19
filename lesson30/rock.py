class Rock:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def get_info(self):
        return f"{self.name}, {self.color}, {self.size}"

