#Assignment: Temperature Converter
#Class: Python D80
#Date: 4/10/25
#Name: Angie Campos

# write welcome message
print()
print("Angie's Temparature Converter" )
print()

while True:
    # Get temp input and temp type
    # Continues to prompt until user enters 00
    fTemp = float(input("Enter a temperature (00 to exit): "))
    if fTemp == 00:
        break
    sTempType = input("Is the temp F for Fahrenheit or C for Celsius? ")

# Calculate based on F (-212 up to 212)
    if sTempType == "F" or sTempType == "f":
        if fTemp > 212:
            print("Temp can not be > 212")
        elif fTemp > -212:
            print("Temp can not be < -212")
        else:
            fFahrenheit = (5.0 / 9) * (fTemp - 32)
            print(f"The Fahrenheit equivalent is {fFahrenheit:.1f}")

    # Calculate based on C (-100 up to 100)
    elif  sTempType == "C" or sTempType == "c":
        if fTemp > 100:
            print("Temp can not be > 100")
        elif fTemp > -100:
            print("Temp can not be < -100")
        else:
            fCelsius = ((9.0 / 5.0) * fTemp) + 32
            print(f"The Celsius equivalent is {fCelsius:.1f}")

    # add an error message if no temp type received
    else:
        print("Enter an F or a C")
        raise SystemExit
