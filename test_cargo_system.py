import unittest
import os

from cargo_item import CargoItem
from special_cargo import SpecialCargo
from cargo_station import CargoStation
from cargo_station import CargoNotFoundError, DuplicateCargoError
from file_helper import save_to_file, load_from_file


class TestCargoSystem(unittest.TestCase):
    # Test valid cargo item creation
    def test_valid_cargo_creation(self):
        item = CargoItem(101, "Oxygen Tank", 12.5, "Mars")

        self.assertEqual(item.item_id, 101)
        self.assertEqual(item.name, "Oxygen Tank")
        self.assertEqual(item.weight, 12.5)
        self.assertEqual(item.origin_planet, "Mars")

    # Test invalid weight
    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            CargoItem(101, "Oxygen Tank", -5, "Mars")

    # Test invalid name
    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            CargoItem(101, "A", 12.5, "Mars")

    # Test valid special cargo creation
    def test_valid_special_cargo_creation(self):
        item = SpecialCargo(201, "Fuel Cell", 30.5, "Venus", 4, True)

        self.assertEqual(item.item_id, 201)
        self.assertEqual(item.name, "Fuel Cell")
        self.assertEqual(item.weight, 30.5)
        self.assertEqual(item.origin_planet, "Venus")
        self.assertEqual(item.danger_level, 4)
        self.assertEqual(item.requires_cooling, True)

    # Test invalid danger level
    def test_invalid_danger_level(self):
        with self.assertRaises(ValueError):
            SpecialCargo(201, "Fuel Cell", 30.5, "Venus", 8, True)

    # Test duplicate item id prevention
    def test_duplicate_item_id(self):
        station = CargoStation()

        item1 = CargoItem(101, "Oxygen Tank", 12.5, "Mars")
        item2 = CargoItem(101, "Food Box", 8, "Earth")

        station.add_item(item1)

        with self.assertRaises(DuplicateCargoError):
            station.add_item(item2)

    # Test removing missing item
    def test_remove_missing_item(self):
        station = CargoStation()

        with self.assertRaises(CargoNotFoundError):
            station.remove_item(999)

    # Test total weight calculation
    def test_total_weight(self):
        station = CargoStation()

        item1 = CargoItem(101, "Oxygen Tank", 12.5, "Mars")
        item2 = CargoItem(102, "Food Box", 8, "Earth")

        station.add_item(item1)
        station.add_item(item2)

        self.assertEqual(station.get_total_weight(), 20.5)

    # Test file save and load behavior
    def test_file_save_and_load(self):
        filename = "test_cargo_data.txt"

        items = [
            CargoItem(101, "Oxygen Tank", 12.5, "Mars"),
            SpecialCargo(201, "Fuel Cell", 30.5, "Venus", 4, True)
        ]

        save_result = save_to_file(filename, items)
        loaded_items = load_from_file(filename)

        self.assertEqual(save_result, True)
        self.assertEqual(len(loaded_items), 2)
        self.assertEqual(loaded_items[0].name, "Oxygen Tank")
        self.assertEqual(loaded_items[1].danger_level, 4)

        if os.path.exists(filename):
            os.remove(filename)

    # Test missing file load safely
    def test_load_missing_file(self):
        loaded_items = load_from_file("missing_file.txt")

        self.assertEqual(loaded_items, [])


if __name__ == "__main__":
    unittest.main()