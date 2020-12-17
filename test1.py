import requests
import json

def test_weather_api():
    response = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    #print(response.json())
    x=response.json();
    #y=json.dumps(x);
    #z=json.loads(y);
    for val in x['list']:
        if(val['weather'][0]['id']==500):
            print(val['weather'][0]['description'])
            # if(val['weather'][0]['description']=='light rain'):
            #     print("found light rain")
            # else:
            #     print("not found light rain")
    for val in x['list']:
        if(val['weather'][0]['id']==800):
            print(val['weather'][0]['description'])
            # if (val['weather'][0]['description'] == 'clear sky'):
            #     print("found clear sky")
            # else:
            #     print("not found clear sky")
    count=0;
    for val in x['list']:
        if(val['main']['temp']>val['main']['temp_min'] and val['main']['temp']<val['main']['temp_max']):
            print(val['main']['temp'])
            count+=1;
    if(count==0):
        print("no temperature present in the range");
re present in the range");