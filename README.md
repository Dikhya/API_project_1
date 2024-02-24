Overview:

This Python script is designed to retrieve and display the current temperature of a specified city using the OpenWeatherMap API. It takes user input for the city name, constructs a URL with the base URL, city name, and API key, sends a GET request to the OpenWeatherMap API, and then processes the response to extract and display the temperature in Celsius.

Features:

1)User Input: It prompts the user to enter the name of the city for which they want to retrieve the weather information.

2)API Integration: The script uses the requests library to make a GET request to the OpenWeatherMap API. It constructs the API URL with the base URL, city name, and API key.

3)Response Handling: It checks the HTTP status code of the response. If the status code is 200 (OK), it proceeds to extract and display the temperature. Otherwise, it prints an error message.

4)Temperature Conversion: The temperature is initially retrieved in Kelvin from the API response. The script then converts it to Celsius by subtracting 273.15.

5)Formatting: The temperature is formatted to display only two decimal places using the format() function.

6)Output: It prints the city name and the current temperature in Celsius, along with a success message if the API request is successful. If there is an error, it prints an error message.

Note: Ensure that the API key is valid and has the necessary permissions to access weather data from OpenWeatherMap. Also, it's good practice to handle potential exceptions that might occur during the execution, such as network errors or invalid JSON responses.
