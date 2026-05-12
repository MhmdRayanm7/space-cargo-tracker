class CargoItem:
    # Create a regular cargo item with validation
    def __init__(self, item_id, name, weight, origin_planet):
        self._item_id = item_id
        self.name = name
        self.weight = weight
        self.origin_planet = origin_planet

    @property
    def item_id(self):
        # item_id is read only after creation
        return self._item_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # name must have at least 2 characters
        if len(value) < 2:
            raise ValueError("Name must be at least 2 characters")
        self._name = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        # weight must be greater than 0
        if value <= 0:
            raise ValueError("Weight must be greater than 0")
        self._weight = value

    @property
    def origin_planet(self):
        return self._origin_planet

    @origin_planet.setter
    def origin_planet(self, value):
        self._origin_planet = value

    def __str__(self):
        # Return cargo item details as text
        return f"CargoItem ID: {self.item_id}, Name: {self.name}, Weight: {self.weight}, Origin: {self.origin_planet}"