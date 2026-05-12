# Space Cargo Tracker

Mid-Semester Project for Object-Oriented Programming in Python.

## Description

Space Cargo Tracker is a small cargo tracking system for a futuristic space station.

The system can:
- Add regular cargo items
- Add special cargo items
- Remove cargo by ID
- Find cargo by ID
- Calculate total cargo weight
- Filter cargo items by origin planet
- Save cargo data to a file
- Load saved cargo data when the program starts
- Log errors into an errors.log file
- Run unit tests using unittest

## Project Files

- `main.py` - menu based program
- `cargo_item.py` - regular cargo item class
- `special_cargo.py` - special cargo class
- `cargo_station.py` - cargo station management and custom exceptions
- `file_helper.py` - save and load cargo data
- `error_logger.py` - error logging
- `test_cargo_system.py` - unit tests

## Bonus Feature

The bonus feature is filtering cargo items by origin planet.

Example:
```python
mars_items = station.filter_by_planet("Mars")