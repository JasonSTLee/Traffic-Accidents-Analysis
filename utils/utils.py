import pandas as pd
import numpy


# Converting string time value to 12-hour clock format
def hour_to_regular_time(hour):
    if hour == '00':
        return '12am'
    elif hour == '01':
        return '1am'
    elif hour == '02':
        return '2am'
    elif hour == '03':
        return '3am'
    elif hour == '04':
        return '4am'
    elif hour == '05':
        return '5am'
    elif hour == '06':
        return '6am'
    elif hour == '07':
        return '7am'
    elif hour == '08':
        return '8am'
    elif hour == '09':
        return '9am'
    elif hour == "10":
        return '10am'
    elif hour == '11':
        return '11am'
    elif hour == '12':
        return '12pm'
    elif hour == '13':
        return '1pm'
    elif hour == '14':
        return '2pm'
    elif hour == '15':
        return '3pm'
    elif hour == '16':
        return '4pm'
    elif hour == '17':
        return '5pm'
    elif hour == '18':
        return '6pm'
    elif hour == '19':
        return '7pm'
    elif hour == '20':
        return '8pm'
    elif hour == '21':
        return '9pm'
    elif hour == '22':
        return '10pm'
    elif hour == '23':
        return '11pm'
    

# Creating rule based logic to assign severity scores to each unique weather condiition value
# 1 = No bother at all
# 2 = Light annoyance
# 3 = Moderate annoyance
# 4 = Dangerous to drive
def custom_weather_sentiment(weather_condition):
    if weather_condition == 'Scattered Clouds':
        return 1
    elif weather_condition == 'Overcast':
        return 1
    elif weather_condition == 'Partly Cloudy':
        return 1
    elif weather_condition == 'Fair':
        return 1
    elif weather_condition == 'Fair / Windy':
        return 1
    elif weather_condition == 'Mostly Cloudy':
        return 1
    elif weather_condition == 'Clear':
        return 1
    elif weather_condition == 'Light Rain':
        return 2
    elif weather_condition == 'Rain':
        return 2
    elif weather_condition == 'Fog':
        return 2
    elif weather_condition == 'Cloudy':
        return 1
    elif weather_condition == 'Smoke':
        return 2
    elif weather_condition == 'Thunderstorm':
        return 4
    elif weather_condition == 'Showers in the Vicinity':
        return 2
    elif weather_condition == 'Shallow Fog':
        return 3
    elif weather_condition == 'Mist':
        return 2
    elif weather_condition == 'Haze':
        return 3
    elif weather_condition == 'Partly Cloudy / Windy':
        return 1
    elif weather_condition == 'Rain Shower':
        return 3
    elif weather_condition == 'Heavy Rain':
        return 3
    elif weather_condition == 'Rain / Windy':
        return 3
    elif weather_condition == 'T-Storm':
        return 4
    elif weather_condition == 'Light Drizzle':
        return 1
    elif weather_condition == 'Light Rain / Windy':
        return 1
    elif weather_condition == 'Light Thunderstorms and Rain':
        return 2
    elif weather_condition == 'Cloudy / Windy':
        return 1
    elif weather_condition == 'Light Snow':
        return 2
    elif weather_condition == 'Heavy T-Storm':
        return 4
    elif weather_condition == 'Mostly Cloudy / Windy':
        return 1
    elif weather_condition == 'Thunder':
        return 4
    elif weather_condition == 'Thunder in the Vicinity':
        return 3
    elif weather_condition == 'Thunderstorms and Rain':
        return 3
    elif weather_condition == 'Rain Shower / Windy':
        return 3
    elif weather_condition == 'Heavy Rain / Windy':
        return 3
    elif weather_condition == 'Patches of Fog':
        return 2
    elif weather_condition == 'Light Rain with Thunder':
        return 2
    elif weather_condition == 'T-Storm / Windy':
        return 4
    elif weather_condition == 'Hail':
        return 3
    elif weather_condition == 'Drizzle':
        return 1
    elif weather_condition == 'Snow':
        return 3
    elif weather_condition == 'Heavy Snow':
        return 4
    elif weather_condition == 'Wintry Mix':
        return 3
    elif weather_condition == 'Light Snow / Windy':
        return 2
    elif weather_condition == 'N/A Precipitation':
        return 2
    elif weather_condition == 'Fog / Windy':
        return 2
    elif weather_condition == 'Partial Fog':
        return 2
    elif weather_condition == 'Heavy Snow':
        return 4
    elif weather_condition == 'Smoke / Windy':
        return 2
    elif weather_condition == 'Light Hail':
        return 3
    elif weather_condition == 'Haze / Windy':
        return 2
    elif weather_condition == 'Light Freezing Fog':
        return 2
    elif weather_condition == 'Light Haze':
        return 2
    elif weather_condition == 'Snow / Windy':
        return 2
    elif weather_condition == 'Widespread Dust / Windy':
        return 4
    elif weather_condition == 'Blowing Dust / Windy':
        return 4
    elif weather_condition == 'Blowing Dust':
        return 3
    elif weather_condition == 'Thunder and Hail':
        return 4
    elif weather_condition == 'LightThunderstorm':
        return 3
    elif weather_condition == 'Heavy Snow / Windy':
        return 4
    elif weather_condition == 'Sand / Windy':
        return 2
    elif weather_condition == 'Squalls / Windy':
        return 2
    elif weather_condition == 'Wintry Mix / Windy':
        return 2
    elif weather_condition == 'Widespread Dust':
        return 4
    elif weather_condition == 'Light Freezing Rain':
        return 2
    elif weather_condition == 'Light Drizzle / Windy':
        return 2
    elif weather_condition == 'Duststorm':
        return 4
    elif weather_condition == 'Light Rain Showers':
        return 2
    elif weather_condition == 'Heavy Thunderstorms and Rain':
        return 4
    elif weather_condition == 'Misty / Windy':
        return 2
    elif weather_condition == 'Thunder / Windy':
        return 3
    elif weather_condition == 'Light Rain Shower':
        return 2
    elif weather_condition == 'Heavy T-Storm / Windy':
        return 4
    elif weather_condition == 'Light Snow Showers':
        return 2
    elif weather_condition == 'Light Snow Shower':
        return 2
    elif weather_condition == 'Snow and Thunder':
        return 4
    elif weather_condition == 'Blowing Snow':
        return 3
    elif weather_condition == 'Small Hail':
        return 3
    elif weather_condition == 'Light Rain Shower / Windy':
        return 2
    elif weather_condition == 'Light Snow with Thunder':
        return 3
    elif weather_condition == 'Squalls':
        return 4
    elif weather_condition == 'Dust Whirls':
        return 4
    elif weather_condition == 'Heavy Drizzle':
        return 2
    elif weather_condition == 'Heavy Rain Shower':
        return 3
    elif weather_condition == 'Blowing Sand':
        return 3
    elif weather_condition == 'Volcanic Ash':
        return 4
    elif weather_condition == 'Rain Showers':
        return 3
    elif weather_condition == 'Mist / Windy':
        return 2
    elif weather_condition == 'Drizzle / Windy':
        return 2
    elif weather_condition == 'Light Thunderstorm':
        return 3
    elif weather_condition == 'Heavy Smoke':
        return 4
    else:
        return weather_condition


# Visibility sentiment
# 1 = Great visibility
# 2 = Good 
# 3 = Moderate
# 4 = Poor 
def custom_visibilty_sentiment(visibility):
    if visibility >= 10:
        return 1
    elif 5 < visibility < 10:
        return 2
    elif 2 <= visibility <= 5:
        return 3
    elif visibility < 2:
        return 4
    
    
# Precipitation sentiment 
# 1 = No Rain
# 2 = Low
# 3 = Moderate
# 4 = Heavy
def custom_precipitation_sentiment(precipitation):
    if precipitation >= 0.3:
        return 4
    elif 0.1 < precipitation < 0.3:
        return 3
    elif 0 < precipitation <= 0.1:
        return 2
    elif precipitation == 0.:
        return 1
    else:
        return 1
    
    
# Snow sentiment 
# 1 = No Snow
# 2 = Low
def custom_snow_sentiment(snow):
    if snow == 0:
        return 1
    else:
        return 2
    
    
# Function to modify weather columns 
def weather_sentiment_func(df, weather_col, visibility_col, precipitation_col,
                      weather_func, visibility_func, precipitation_func):
    
    df[weather_col] = df[weather_col].apply(weather_func)
    df[visibility_col] = df[weather_col].apply(visibility_func)
    df[precipitation_col] = df[weather_col].apply(precipitation_func)
    
    return df


# Similar to SQL's row number function, returns the dataframe with new row numbers
def row_num(df, column, ascending = False):
    sort_df = df.sort_values(by = column, ascending = ascending)
    sort_df['rn_' + column] = sort_df.reset_index().index + 1

    return sort_df