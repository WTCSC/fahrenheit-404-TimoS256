try:
    unit = float(input("Enter 1 for C to F, Enter 2 for F to C:"))

except:
    print('You must enter "1" or "2"')
    quit()
try: 
    value = float(input("Enter temperature to be converted:"))
except:
    print("Must be a number")
    quit()
if unit == 1:
    print(f"{value}°C is equal to {(value * 1.8) + 32}°F")
else:
    print(f"{value}°F is equal to {(value - 32) * 0.5555}°C")

