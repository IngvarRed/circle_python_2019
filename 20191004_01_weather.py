# python per hour . weather assistant

import pyowm

owm = pyowm.OWM('a94912d827ff0f958082238e40144c1f')  # You MUST provide a valid API key

place = input("Are you interested in weather conditions? \nWrite your City/Country : ")

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place(place)
w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20, status=Clouds>

temp = w.get_temperature('celsius')["temp"]

print("Weather condition is ..")
print("In city " + place + " now is " + w.get_detailed_status())
print("ambient temperature now is " + str(temp))

print("\nMy recommendations : ")
if temp < 10:
    print("    - It's cold outside, dress warmly! ")
elif temp < 20:
    print("    - It's cool now, dress warmer ;-) ")
else:
    print("    - Get warm outside, wear whatever you want :-) ")
