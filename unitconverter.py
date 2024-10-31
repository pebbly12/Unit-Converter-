# Function for converting length
def convert_length(value, from_unit, to_unit):
    # Conversion factors
    conversion_factors_for_length = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
    }
    
    # Convert value to meters
    value_in_meters = value * conversion_factors_for_length[from_unit]
    # Convert from meters to target unit
    return value_in_meters / conversion_factors_for_length[to_unit]


# Function for converting weight
def convert_weight(value, from_unit, to_unit):
    # Conversion factors
    conversion_factors_for_weight = {
        'grams': 1,
        'kilograms': 1000,
        'milligrams': 0.001
}
    # Convert value to grams
    value_in_grams = value * conversion_factors_for_weight[from_unit]
    return value_in_grams / conversion_factors_for_weight[to_unit]


# Function for converting volume
def convert_volume(value, from_unit, to_unit):
    # Conversion factors 
    conversion_factors_for_volume = {
        'liters': 1,
        'millimeters': 1000,
        'cubic meters':1000
    }

    # Convert value to liters
    value_in_liters = value * conversion_factors_for_volume[from_unit]
    return value_in_liters / conversion_factors_for_volume[to_unit]

# Function for converting temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

# Main loop
def UnitConverter():
    print("Welcome to the Unit Converter!")

    while True:
        print("\nPlease select the type of conversion you want to perform:")
        print("1. Length")
        print("2. Weight")
        print("3. Volume")
        print("4. Temperature")
        print("5. Exit")

        options = int(input("Please select an option (1-5): "))
        # Length conversion 
        if options == 1:
            print("\n--- Length Converter ---")
            value = float(input("Please enter the value you want to convert: "))
            from_unit = input("Please enter the unit you are converting from (meters, kilometers, miles): ").strip().lower()
            to_unit = input("Please enter the unit you want to convert to (meters, kilometers, miles): ").strip().lower()

            result = convert_length(value,from_unit,to_unit)
            print(f"Converting {value} {from_unit} to {to_unit}.....")
            print(f"{value} {from_unit} equal to {result:.4f} {to_unit}.")

        # Weight conversion 
        elif options == 2:
            print("\n--- Weight Converter ---")
            value = float(input("Please enter the value you want to convert: "))
            from_unit = input("Please enter the unit you are converting from (grams, kilograms, milligrams): ").strip().lower()
            to_unit = input("Please enter the unit you want to convert to (grams, kilograms, milligrams): ").strip().lower()

            result = convert_weight(value,from_unit,to_unit)
            print(f"Converting {value} {from_unit} to {to_unit}.....")
            print(f"{value} {from_unit} equal to {result:.4f} {to_unit}.")

        # Volume conversion 
        elif options == 3:
            print("\n--- Volume Converter ---")
            value = float(input("Please enter the value you want to convert: "))
            from_unit = input("Please enter the unit you are converting from (liters, millimeters, cubic meters): ").strip().lower()
            to_unit = input("Please enter the unit you want to convert to (liters, millimeters, cubic meters): ").strip().lower()

            result = convert_volume(value,from_unit,to_unit)
            print(f"Converting {value} {from_unit} to {to_unit}.....")
            print(f"{value} {from_unit} equal to {result:.4f} {to_unit}.")

        # Temperatur conversion 
        elif options == 4:
            print("\n--- Temperature Converter ---")
            value = float(input("Please enter the value you want to convert: "))
            from_unit = input("Please enter the unit you are converting from (celsius, fahrenhiet, kelvin): ").strip().lower()
            to_unit = input("Please enter the unit you want to convert to (celsius, fahrenhiet, kelvin): ").strip().lower()

            result = convert_temperature(value,from_unit,to_unit)
            print(f"Converting {value} {from_unit} to {to_unit}.....")
            print(f"{value} {from_unit} equal to {result:.4f} {to_unit}.")

        # Exiting the unit conveter 
        elif options == 5:
            print("Thank you for using the Unit Converter! Goodbye!")
            return 
                    
        else:
            print("Invalid input!")

if __name__== "__main__":
    UnitConverter()
    another_conversion = input("\nDo you want to perform another conversion? (yes/no): ").strip().lower()
    if another_conversion != 'yes':
        print("Thank you for using the Unit Converter! Goodbye!")

            







