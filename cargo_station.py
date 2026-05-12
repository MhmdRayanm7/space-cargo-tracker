from cargo_item import CargoItem


class CargoNotFoundError(Exception):
    # Raised when cargo item is not found
    pass


class DuplicateCargoError(Exception):
    # Raised when cargo item already exists
    pass


class InvalidCargoError(Exception):
    # Raised when object is not CargoItem
    pass


class CargoStation:
    # Manage all cargo items in the station
    def __init__(self):
        self._items = []

    def add_item(self, item):
        # Add cargo item if it is valid and not duplicate
        if not isinstance(item, CargoItem):
            raise InvalidCargoError("Only CargoItem objects can be added")

        if self.find_item(item.item_id) is not None:
            raise DuplicateCargoError("Item already exists")

        self._items.append(item)

    def remove_item(self, item_id):
        # Remove cargo item by item_id
        for item in self._items:
            if item.item_id == item_id:
                self._items.remove(item)
                return item

        raise CargoNotFoundError("Item was not found")

    def find_item(self, item_id):
        # Find cargo item by item_id
        for item in self._items:
            if item.item_id == item_id:
                return item

        return None

    def get_total_weight(self):
        # Return total weight of all cargo items
        total = 0

        for item in self._items:
            total += item.weight

        return total

    def get_all_items(self):
        # Return all cargo items
        return self._items