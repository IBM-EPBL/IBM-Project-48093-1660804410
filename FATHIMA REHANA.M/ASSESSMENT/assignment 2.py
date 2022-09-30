
import os
import requests
from datetime import datetime

user_api=os.environ['current_weather_data']
location=input("enter the city name:")


complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link= requests.get(complete_api_link)
api_data=api_link.json()
print(api_data)


if api_data['cod']=='404':
    print ("invalid city:{},please check your city name.".format(location))
else:
        temp_city =((api_data['main']['temp']) -273.15)
        weather_desc=api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd=api_data['wind']['speed']
        date_time = datetime.now().strftime("%d  %b %y|%I %M %S %p")

        print("------------------------------------------------")
        print("weather status for -{} || {}".format(location.upper(),date_time))
        print("------------------------------------------------")
        
        print("current temperature is :{:.2f} deg c".format(temp_city))

        
        print("current weather desc:",weather_desc)
            
        print ("current wind speed :",wind_spd,'kmph')
        
        print("current humidity:",hmdt,'%')
if hmdt >=50:
    
    print (" high humid")
else:
    print(" low humidity")
    
if temp_city > 25:
        print("temperature is high")
else:
        print("temperature is low")
        

 



