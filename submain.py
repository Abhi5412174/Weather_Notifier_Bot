import requests
from twilio.rest import Client

# Weather API configuration
API_KEY = 'Place_your_openweathermap_api_key_here'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Twilio configuration
ACCOUNT_SID = 'Place_your_twilio_account_sid' 
AUTH_TOKEN = 'Place_your_twilio_auth_token' 
TWILIO_PHONE_NUMBER = 'Place_your_twilio_phone_number'

def get_weather(city):
    """Fetch current weather data for the given city."""
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def send_sms(to_phone_number, message):
    """Send SMS notification with weather info using Twilio."""
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=to_phone_number
    )
    print(f"SMS sent to {to_phone_number}")

def generate_suggestions(weather_data):
    """Generate activity or clothing suggestions based on weather conditions."""
    weather_main = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp']

    if weather_main in ['Rain', 'Drizzle']:
        return "It's raining! Don't forget your umbrella. Maybe stay indoors or enjoy a cozy café."
    elif weather_main == 'Clear':
        if temp > 25:
            return "It's a sunny day! Perfect for outdoor activities like a picnic or walk in the park. Wear light clothes."
        else:
            return "Clear skies! It might be a bit cool, so bring a jacket if you're going out."
    elif weather_main == 'Snow':
        return "It's snowing! Time for warm clothes and maybe some hot cocoa. Perfect day for indoor activities."
    elif weather_main == 'Clouds':
        return "It's cloudy today. Great for a relaxing day, maybe a book or light outdoor activities."
    else:
        return "Weather is a bit unpredictable today. Check before going out!"