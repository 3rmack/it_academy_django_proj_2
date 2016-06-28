from django.shortcuts import render
from forms import CityForm, StreetForm, SearchForm
from models import Cities, Streets
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def city_form(request):
    context = {'city_form': CityForm()}
    return render(request, 'city_form.html', context)


def city_form_post(request):
    raw_data = CityForm(request.POST)
    if raw_data.is_valid():
        data = raw_data.cleaned_data
        # print data
        city = Cities.objects.create(**data)
        return street_form(request, city)
    data = raw_data.errors
    return HttpResponse('{0}'.format(data))


def street_form(request, city):
    context = {'street_form': StreetForm(), 'city': city}
    return render(request, 'street_form.html', context)


def street_form_post(request):
    raw_data = StreetForm(request.POST)
    if raw_data.is_valid():
        data = raw_data.cleaned_data
        city_id = request.POST.get('city_id')
        city_name = request.POST.get('city_name')
        # print data, city_id
        street = Streets.objects.create(city_id=city_id, **data)
        # return HttpResponse('ok')
        context = {'city_id': city_id, 'city_name': city_name, 'street': street}
        return render(request, 'result_page.html', context)
    data = raw_data.errors
    return HttpResponse('{0}'.format(data))


def street_form_post_one_more(request):
    city_id = request.POST.get('city_id')
    city_name = request.POST.get('city_name')
    return street_form(request, city_id)


def search_form(request):
    context = {'search_form': SearchForm()}
    return render(request, 'search_form.html', context)
