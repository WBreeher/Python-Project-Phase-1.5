# This is a function-driven Temperature Converter.
import sys

print("\nThis is a function-driven Temeperature Converter.  Created by W.Breeher. Nov 13th, 2025\n")
print("\nYou can type Leave at any point to end the program.\n")

# === Functions ===
def fah(a):
    """Returns Fahrenheit to Celsius"""
    return (a - 32) / 1.8

def cel(a):
    """Returns Celsius to Fahrenheit"""
    return (a * 1.8) + 32

def kelf(a):
    """Return Fahrenheit to Kelvin"""
    return (a - 32) * (5/9) + 273.15

def kelc(a):
    """Return Celsius to Kelvin"""
    return (a + 273.15)

def leave():
    """Ends Program"""
    sys.exit("Program ended. Have a good day.")

# === Program ===
while True:
    try:
        op = input("\nPlease enter starting temperature model: Fah, Cel, KelF, KelC ").strip().lower()
        if op == "leave":
            leave()

        a = float(input("Enter starting temperature: "))

        if op == "fah":
            print(f"{fah(a):.1f}°C")

        if op == "cel":
            print(f"{cel(a):.1f}°F")

        if op == "kelf":
            print(f"{kelf(a):.2f}K")

        if op == "kelc":
            print(f"{kelc(a):.2f}K")

    except ValueError:
        print("Invalid Entry, please try again.")
