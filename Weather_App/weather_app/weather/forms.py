from django.forms import ModelForm, TextInput
from .models import City 
from . import views
#from .views import city_weather

class CityForm(ModelForm):
    class Meta:
        
        # #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

        # cities = City.objects.all()

        # for city in cities:

        #     r = requests.get(url.format(city)).json()

        #     city_weather = {
        #         'city': city.name,
        #         'temperature': r['main']['temp'],
        #         'description': r['weather'][0]['description'],
        #     }
            


        model = City 
        fields = ['name'] 
        # city_weather['temperature'] = ['temperature']
        # city_weather['description'] = ['description']

        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
        #widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
