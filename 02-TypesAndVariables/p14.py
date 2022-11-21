def temp(degrees):
    kelvin = degrees + 273.15
    fahrenheit = degrees * 1.8 + 32

    return (f"Kelvin: {kelvin}, Fahrenheit: {fahrenheit}")


degrees = float(input("Enter degrees in Celcius: "))
print(temp(degrees))