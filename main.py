class Vehicle:
    def __init__(self, type, fuel):
        self.type = type
        self.fuel = fuel

    def __init__(self, type):
        self.type = type


Car = Vehicle('car')
