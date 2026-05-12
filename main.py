from cargo_item import CargoItem
from special_cargo import SpecialCargo
from cargo_station import CargoStation
from cargo_station import CargoNotFoundError, DuplicateCargoError, InvalidCargoError
from file_helper import save_to_file, load_from_file
from error_logger import log_error


def print_menu():
    # Print the main menu options
    print()
    print("1 Add cargo")
    print("2 Remove cargo")
    print("3 Find cargo")
    print("4 Show total weight")
    print("5 Show all cargo")
    print("6 Save and exit")


def add_cargo(station):
    # Add regular or special cargo to the station
    cargo_type = input("Enter cargo type regular/special: ")

    item_id = int(input("Enter item id: "))
    name = input("Enter name: ")
    weight = float(input("Enter weight: "))
    origin_planet = input("Enter origin planet: ")

    if cargo_type == "regular":
        item = CargoItem(item_id, name, weight, origin_planet)

    elif cargo_type == "special":
        danger_level = int(input("Enter danger level 1-5: "))
        cooling_input = input("Requires cooling yes/no: ")

        requires_cooling = cooling_input == "yes"

        item = SpecialCargo(
            item_id,
            name,
            weight,
            origin_planet,
            danger_level,
            requires_cooling
        )

    else:
        raise ValueError("Cargo type must be regular or special")

    station.add_item(item)
    print("Cargo added successfully")


def remove_cargo(station):
    # Remove cargo item by id
    item_id = int(input("Enter item id to remove: "))

    removed_item = station.remove_item(item_id)

    print("Removed:")
    print(removed_item)


def find_cargo(station):
    # Find cargo item by id
    item_id = int(input("Enter item id to find: "))

    item = station.find_item(item_id)

    if item is None:
        raise CargoNotFoundError("Item was not found")

    print(item)


def show_total_weight(station):
    # Print total weight of all cargo
    print("Total weight:", station.get_total_weight())


def show_all_cargo(station):
    # Print all cargo items
    items = station.get_all_items()

    if len(items) == 0:
        print("No cargo items found")
    else:
        for item in items:
            print(item)


def load_items_to_station(station):
    # Load saved items when the program starts
    items = load_from_file("cargo_data.txt")

    for item in items:
        station.add_item(item)


def main():
    # Run the cargo station menu program
    station = CargoStation()

    try:
        load_items_to_station(station)
    except Exception as error:
        log_error(error, "load_items_to_station")

    choice = ""

    while choice != "6":
        print_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_cargo(station)

            elif choice == "2":
                remove_cargo(station)

            elif choice == "3":
                find_cargo(station)

            elif choice == "4":
                show_total_weight(station)

            elif choice == "5":
                show_all_cargo(station)

            elif choice == "6":
                save_to_file("cargo_data.txt", station.get_all_items())
                print("Data saved. Goodbye!")

            else:
                print("Invalid choice")

        except ValueError as error:
            print("Input error:", error)
            log_error(error, "main menu")

        except CargoNotFoundError as error:
            print("Cargo error:", error)
            log_error(error, "main menu")

        except DuplicateCargoError as error:
            print("Cargo error:", error)
            log_error(error, "main menu")

        except InvalidCargoError as error:
            print("Cargo error:", error)
            log_error(error, "main menu")

        except Exception as error:
            print("Unexpected error:", error)
            log_error(error, "main menu")


main()