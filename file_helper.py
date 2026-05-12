from cargo_item import CargoItem
from special_cargo import SpecialCargo


def save_to_file(filename, cargo_list):
    # Save cargo items to a text file
    try:
        file = open(filename, "w")

        for item in cargo_list:
            if isinstance(item, SpecialCargo):
                line = f"special,{item.item_id},{item.name},{item.weight},{item.origin_planet},{item.danger_level},{item.requires_cooling}\n"
            else:
                line = f"regular,{item.item_id},{item.name},{item.weight},{item.origin_planet}\n"

            file.write(line)

        file.close()

    except Exception:
        # Prevent program crash during saving
        return False

    return True


def load_from_file(filename):
    # Load cargo items from a text file
    cargo_list = []

    try:
        file = open(filename, "r")

        for line in file:
            line = line.strip()

            if line == "":
                continue

            parts = line.split(",")

            if parts[0] == "regular":
                item = CargoItem(
                    int(parts[1]),
                    parts[2],
                    float(parts[3]),
                    parts[4]
                )
                cargo_list.append(item)

            elif parts[0] == "special":
                item = SpecialCargo(
                    int(parts[1]),
                    parts[2],
                    float(parts[3]),
                    parts[4],
                    int(parts[5]),
                    parts[6] == "True"
                )
                cargo_list.append(item)

        file.close()

    except FileNotFoundError:
        # If file does not exist, return empty list
        return []

    except Exception:
        # If file is empty or damaged, return empty list
        return []

    return cargo_list