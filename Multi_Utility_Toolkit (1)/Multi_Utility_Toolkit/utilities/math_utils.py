"""Additional mathematical utilities for the toolkit."""


def km_to_miles(kilometres):
    """Convert kilometres to miles."""
    return kilometres * 0.621371


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def simple_percentage(value, percentage):
    """Return a percentage of a given value."""
    return value * percentage / 100


if __name__ == "__main__":
    print("10 km in miles:", km_to_miles(10))
