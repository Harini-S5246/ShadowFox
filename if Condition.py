print("=== BMI Calculator ===")
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")
print()

print("=== City to Country ===")
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print(f"{city} not found in our database")
print()

print("=== Check if two cities in same country ===")
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in australia:
    country1 = "Australia"
elif city1 in uae:
    country1 = "UAE"
elif city1 in india:
    country1 = "India"
else:
    country1 = "Unknown"

if city2 in australia:
    country2 = "Australia"
elif city2 in uae:
    country2 = "UAE"
elif city2 in india:
    country2 = "India"
else:
    country2 = "Unknown"

if country1 == country2 and country1 != "Unknown":
    print(f"Both cities are in {country1}")
elif country1 == "Unknown" or country2 == "Unknown":
    print("One or both cities not found in our database")
else:
    print("They don't belong to the same country")