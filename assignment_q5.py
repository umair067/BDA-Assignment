print("Press C to convert from Fahrenheit to Celsius.")
print("Press F to convert from Celsius to Fahrenheit.")
your_choice = str.upper(input("Your choice: "))
if your_choice == "C" :
    starting_temperature = float(input("Please enter the temperature in Fahrenheit: "))
    temperature_celsius = (starting_temperature-32)*5/9
    print(f"The temperature in Celsius is {temperature_celsius}")
elif your_choice == "F" :
     starting_temperature = float(input("Please enter the temperature in Celcius: "))
     temperature_Fahrenheit = (starting_temperature * 9/5) + 32
     print(f"The temperature in Fahrenheit is {temperature_Fahrenheit} ")
