"""
Resistor colour code calculator.
Reads the colour bands of a 4-band resistor and returns its resistance.

Colour values follow the standard IEC resistor colour code.
"""

COLORS = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "grey": 8, "gray": 8, "white": 9,
}

TOLERANCE = {"brown": 1, "red": 2, "gold": 5, "silver": 10}


def colour_value(colour):
    """Return the digit for a colour name."""
    key = colour.strip().lower()
    if key not in COLORS:
        raise ValueError(f"Unknown colour: {colour!r}")
    return COLORS[key]


def calculate(band1, band2, multiplier, tolerance=None):
    """Return (resistance_in_ohms, tolerance_percent_or_None)."""
    significant = colour_value(band1) * 10 + colour_value(band2)
    value = significant * (10 ** colour_value(multiplier))

    tol = None
    if tolerance:
        tol = TOLERANCE.get(tolerance.strip().lower())
        if tol is None:
            raise ValueError(f"Unknown tolerance colour: {tolerance!r}")
    return value, tol


def format_ohms(value):
    """Format a resistance value with a sensible unit."""
    if value >= 1_000_000:
        return f"{value / 1_000_000:g} MΩ"
    if value >= 1_000:
        return f"{value / 1_000:g} kΩ"
    return f"{value:g} Ω"


def main():
    print("Resistor Colour Code Calculator (4-band)")
    print("Colours: " + ", ".join(sorted(COLORS)))
    print("Tolerance colours: " + ", ".join(sorted(TOLERANCE)))
    print()

    band1 = input("Band 1: ")
    band2 = input("Band 2: ")
    multiplier = input("Multiplier: ")
    tolerance = input("Tolerance (press Enter to skip): ").strip() or None

    try:
        value, tol = calculate(band1, band2, multiplier, tolerance)
    except ValueError as error:
        print(f"\nError: {error}")
        return

    result = format_ohms(value)
    if tol is not None:
        result += f" ±{tol}%"
    print(f"\nResistance: {result}")


if __name__ == "__main__":
    main()
