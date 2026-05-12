from cargo_item import CargoItem


class SpecialCargo(CargoItem):
    # Create special cargo item with danger level and cooling option
    def __init__(self, item_id, name, weight, origin_planet, danger_level, requires_cooling):
        super().__init__(item_id, name, weight, origin_planet)
        self.danger_level = danger_level
        self.requires_cooling = requires_cooling

    @property
    def danger_level(self):
        return self._danger_level

    @danger_level.setter
    def danger_level(self, value):
        # danger level must be between 1 and 5
        if value < 1 or value > 5:
            raise ValueError("Danger level must be between 1 and 5")
        self._danger_level = value

    @property
    def requires_cooling(self):
        return self._requires_cooling

    @requires_cooling.setter
    def requires_cooling(self, value):
        # requires_cooling must be True or False
        if type(value) != bool:
            raise ValueError("Requires cooling must be True or False")
        self._requires_cooling = value

    def __str__(self):
        # Return special cargo item details as text
        return f"SpecialCargo ID: {self.item_id}, Name: {self.name}, Weight: {self.weight},
         Origin: {self.origin_planet}, Danger Level: {self.danger_level}, Requires Cooling: {self.requires_cooling}"