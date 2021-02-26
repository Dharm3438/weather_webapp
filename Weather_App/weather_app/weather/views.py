import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm


# Create your views here.
def index(request):


	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

	err_msg = ""
	message = ""
	message_class = ""
	#final_city = ''
	status = 0
	#new_city = ''

	if request.method == 'POST':
		form = CityForm(request.POST)

		if form.is_valid():
			new_city = form.cleaned_data['name']
			print('\n\n\n\n\n')
			print(new_city)
			existing_city_count = City.objects.filter(name=new_city).count()
			if existing_city_count == 0:
				r = requests.get(url.format(new_city)).json()
				#print(r)
				if r['cod'] == 200:
					status = 1
					final_city = new_city
					print(final_city)
					form.save()
				else:
					err_msg = 'City not found'
			else:
				err_msg = "City Already Exists"
		if err_msg:
			message = err_msg
			message_class = 'is-danger'
		else:
			message = 'City Added Successfully'
			message_class = 'is-success'

	print(err_msg)
	form = CityForm()

	cities = City.objects.all()

	weather_data = []

	for city in cities:


		r = requests.get(url.format(city)).json()
		#print(r.text)

		city_weather = {
			'city': city.name,
			'temperature': r['main']['temp'],
			'description': r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],
		}

		weather_data.append(city_weather)

		#print(city_weather)

	if(status==1):
		if(new_city == final_city):
			entry = City.objects.get(name=final_city)
			entry.temperature = city_weather['temperature']
			entry.description = city_weather['description']
			entry.save()

	#print(weather_data)
	context = {
	'weather_data': weather_data, 
	'form': form,
	'message': message,
	'message_class': message_class,
	} 
	return render(request, 'weather/weather.html', context)


def delete_city(request, city_name):
	City.objects.get(name=city_name).delete()
	return redirect('home')


def clear_all(request):
	City.objects.clear_all()
	return redirect('home')
