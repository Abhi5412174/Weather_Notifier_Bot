#Weather notifier bot using twilio
from submain import get_weather, generate_suggestions, send_sms

def main():
    city = input("Enter your city: ").strip()
    phone_number = input("Enter your phone number (with country code) to receive weather updates via SMS: ").strip()

    # Fetch weather data
    weather_data = get_weather(city)

    if weather_data['cod'] != 200:
        print(f"Error fetching weather data: {weather_data['message']}")
        return

    # Extract weather information
    temp = weather_data['main']['temp']
    weather_desc = weather_data['weather'][0]['description']

    # Generate activity or clothing suggestions
    suggestions = generate_suggestions(weather_data)

    # Prepare SMS message
    message = (f"Current temperature: {temp}°C\n"
               f"Weather condition: {weather_desc.capitalize()}\n\n"
               f"Suggestions: {suggestions}")

    # Send SMS notification
    send_sms(phone_number, message)

if __name__ == "__main__":
    main()
