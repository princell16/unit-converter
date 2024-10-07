import sys

def convert_length(value, from_unit, to_unit):
    # Conversion factors (to meters)
    length_units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }
    
    # Convert to meters, then to desired unit
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Conversion factors (to kilograms)
    weight_units = {
        "mg": 0.000001,
        "g": 0.001,
        "kg": 1,
        "t": 1000,
        "oz": 0.0283495,
        "lb": 0.453592,
        "st": 6.35029
    }
    
    # Convert to kilograms, then to desired unit
    kg = value * weight_units[from_unit]
    return kg / weight_units[to_unit]

def convert_volume(value, from_unit, to_unit):
    # Conversion factors (to liters)
    volume_units = {
        "ml": 0.001,
        "l": 1,
        "m3": 1000,
        "fl oz": 0.0295735,
        "pt": 0.473176,
        "qt": 0.946353,
        "gal": 3.78541
    }
    
    # Convert to liters, then to desired unit
    liters = value * volume_units[from_unit]
    return liters / volume_units[to_unit]

def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        print("\nSelect conversion type:")
        print("1. Length")
        print("2. Weight")
        print("3. Volume")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '4':
            print("Thank you for using the Unit Converter. Goodbye!")
            sys.exit()
        
        value = float(input("Enter the value to convert: "))
        
        if choice == '1':
            from_unit = input("Enter the unit to convert from (mm, cm, m, km, in, ft, yd, mi): ")
            to_unit = input("Enter the unit to convert to (mm, cm, m, km, in, ft, yd, mi): ")
            result = convert_length(value, from_unit, to_unit)
        elif choice == '2':
            from_unit = input("Enter the unit to convert from (mg, g, kg, t, oz, lb, st): ")
            to_unit = input("Enter the unit to convert to (mg, g, kg, t, oz, lb, st): ")
            result = convert_weight(value, from_unit, to_unit)
        elif choice == '3':
            from_unit = input("Enter the unit to convert from (ml, l, m3, fl oz, pt, qt, gal): ")
            to_unit = input("Enter the unit to convert to (ml, l, m3, fl oz, pt, qt, gal): ")
            result = convert_volume(value, from_unit, to_unit)
        else:
            print("Invalid choice. Please try again.")
            continue
        
        print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

if __name__ == "__main__":
    main()
