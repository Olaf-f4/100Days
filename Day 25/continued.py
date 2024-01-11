import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
#print(data_dict)

temp_list = data["temp"].to_list()
#print(temp_list)


def avg():

    # Avg of sum
    print(sum(temp_list) / len(temp_list))

    # Max Value
    print(data["temp"].max())


def row_info():

    # Max Temp
    print(data[data.temp == data.temp.max()])


def create_dataframe():

    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }

    data = pandas.DataFrame(data_dict)
    print(data)

    data.to_csv("new_data.csv")


def squirrel_color():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    list = data.to_dict()
    column = list["Primary Fur Color"]

    Gray = 0
    Cinnamon = 0
    Black = 0
    unknown = 0

    print(column[2])

    for x in column:
        if column[x] == "Gray":
            Gray += 1
        elif column[x] == "Cinnamon":
            Cinnamon += 1
        elif column[x] == "Black":
            Black += 1
        else:
            unknown += 1

    squirrel_stats = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [Gray, Cinnamon, Black]
    }

    stats = pandas.DataFrame(squirrel_stats)
    stats.to_csv("Squirrel Count")
    print(squirrel_stats)


def squirrel_easy():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
    print(gray_squirrel)

    # And so on for the rest of colors :/ ...


row_info()
