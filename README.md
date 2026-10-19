# Resistor Colour Code Calculator
A small Python command-line tool that calculates the resistance value and 
tolerance of a 4-band resistor from its colour bands.

I built this while studying basic electronics — reading colour bands by hand 
is error-prone, so I wrote a script to check my work.

## What it does

You enter the four colour bands (band 1, band 2, multiplier, tolerance) and 
the script returns the resistance with the correct unit (Ω / kΩ / MΩ) and 
tolerance percentage.

## Example
Band 1: brown
Band 2: black
Multiplier: red
Tolerance: gold

Resistance: 1 kΩ ±5%

## How to run it

1. Install Python 3 from python.org
2. Download `resistor_calculator.py`
3. In your terminal:
python resistor_calculator.py

## What I learned

- How the IEC resistor colour code works (two significant digits + multiplier)
- How to structure a small program into functions instead of one long block
- How to handle invalid input with `try` / `except` instead of crashing
- How to format numbers with units so output is readable

## Limitations

- Only supports 4-band resistors, not 5-band precision resistors
- Input is text only — a GUI version would be a better experience
- No automated tests yet — that's the next thing I want to learn
  
