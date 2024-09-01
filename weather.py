# lists to store weather data for a week
temperatures = []
humidities = []
wind_speeds = []

# weather data for each day of the week
for i in range(7):
    print(f"Enter data for day {i + 1}:")

    # Input temperature, humidity, and wind speed
    temp = float(input("Temperature (°F): "))
    humidity = float(input("Humidity (%): "))
    wind_speed = float(input("Wind Speed (km/h): "))

    # Append the data to the lists
    temperatures.append(temp)
    humidities.append(humidity)
    wind_speeds.append(wind_speed)

# Calculate the averages
avg_temp = sum(temperatures) / len(temperatures)
avg_humidity = sum(humidities) / len(humidities)
avg_wind_speed = sum(wind_speeds) / len(wind_speeds)

# Display the results
print("\nWeekly Weather Data Summary:")
print(f"Average Temperature: {avg_temp:.2f} °F")
print(f"Average Humidity: {avg_humidity:.2f} %")
print(f"Average Wind Speed: {avg_wind_speed:.2f} km/h")

