celsius = float(input("Enter the Temperature in celsius: "))

def celsiusToFahrenheitConverter(c):
    f = c * (9/5) +32
    print (f"{c} Celsius = {f} Fahrenheit")

celsiusToFahrenheitConverter(celsius)