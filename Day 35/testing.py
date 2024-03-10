array = [{"dt": 170, "temp":57.7, "pressure":1030,
          "weather":[{
              "id":802,
              "main":"Clouds",
          }]
          }]

for item in array:
    for weather_info in item["weather"]:
        main_value = weather_info["main"]
        print(main_value)

