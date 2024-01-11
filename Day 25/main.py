with open("weather_data.csv", 'r') as r:
    data = r.readlines()
    print(data)

    for x in data:
        print(f"{x}")

# The above would be tough to extract individual elements
# So we import CSV plugin, and allow extracting elements
# to be easier

# List comprehension - need to (n2s)

import csv
with open("weather_data.csv", 'r') as weather:
    data = csv.reader(weather)
    temperatures = []
    for x in data:
        if x[1] != "temp":
            temperatures.append(x[1])
            print(temperatures)

    with open("temperatures_week", 'w') as temp:
        for x in temperatures:
            temp.write(f"{x}\n")

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
