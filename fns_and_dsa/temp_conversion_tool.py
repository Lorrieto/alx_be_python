FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp_to_convert = float(input("Enter the temperature to convert: "))
celsius_Fahrenheit = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):"))

def convert_to_celsius(fahrenheit):
    if(celsius_Fahrenheit == "F"):
       fahrenheit = (temp_to_convert-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
       print(f"{temp_to_convert}°F is {fahrenheit}°C")
    else:
        print("Invalid Input")
convert_to_celsius(temp_to_convert)

def convert_to_fahrenheit(celsius):
    if(celsius_Fahrenheit == "C"):
       celcius = (temp_to_convert * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
       print(f"{temp_to_convert}°F is {celcius}°C")
    else:
        print("Invalid Input")
       
convert_to_fahrenheit(temp_to_convert)
   
