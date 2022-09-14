def measurements(wind_chill):
    air_temp = float(input("air temp: "))
    wind_speed = float(input("wind speed: "))
    print(f"Windchill: {wind_chill}")
    return air_temp, wind_speed

def windchill(air_temp, wind_speed):
    wind_chill = 35.74 + 0.6215 * air_temp - 35.75 *  wind_speed**0.16 + 0.4275 * air_temp * wind_speed**0.16
    print(f"Temperature of {air_temp} and speed of {wind_speed} gives windchill of: {wind_chill}")
    return wind_chill
    

if __name__ == '__main__':
    wind_chill = windchill(10, 15)
    wind_chill = windchill(0, 25)
    wind_chill = windchill(-10, 35)
    air_temp, wind_speed = measurements(wind_chill)
