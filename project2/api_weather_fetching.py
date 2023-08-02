import requests
base_url="https://api.openweathermap.org/data/2.5/weather?q="
api_key="d0247993b0eb17abe143edbb9244049b"  #generate api key from OWM website
city_inp=input("Enter the city name:")      #user input
url=base_url+city_inp+"&appid="+api_key     #complete url generate

response=requests.get(url)                  #Sending a GET request to the API


if(response.status_code==200):
    #print(response.json())
    city_data=response.json()                # Using data from the above response in json format,if it is successful or not. 
   
    city_temp=city_data['main']['temp']         # taking only temp from json data
    #print(city_temp)
    kelvin=273.15                               #converting temp. from  Kelvin to Celsius
    temp=city_temp-kelvin
    new_temp=format(temp,".2f")
    #print(new_temp)
    print("The temperature in "+city_inp+" is "+new_temp+chr(176)+"C")  #by using chr() function to print degree symbol and the numeric point for the degree symbol is 176.
    print("Successfully fetched..!")

else:
    print("Error in fetching data..!")
    print("Please Try Again...")