from models.item import Item

class InMemoryDB:
    def __init__(self):
        self.items: list[Item] = []
