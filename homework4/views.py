# coding: UTF-8
from django.shortcuts import render
from forms import CityForm, StreetForm, SearchForm
from models import Cities, Streets
from django.http import HttpResponse


def index(request):  # первая страница с линками на функции
    return render(request, 'index.html')


def city_form(request):    # рендер страницы с POST запросом для добавления города
    context = {'city_form': CityForm()}
    return render(request, 'city_form.html', context)


def city_form_post(request):  # обработка POST запроса из формы добавления города
    raw_data = CityForm(request.POST)
    if raw_data.is_valid():
        data = raw_data.cleaned_data

        cities_in_db = Cities.objects.filter().values_list()  # получаем список кортежей values городов из бащы
        cities_in_db_list = []  # создание пустого списка названий городов
        for item in cities_in_db:  # обходим все кортежи в списке
            cities_in_db_list.append(item[1])  # нас интересует только второй элемент в кортеже (который name), добавляем его в список

        # проверка есть ли полученный город из формы списке названий городов, которые уже есть в базе
        if data['name'] in cities_in_db_list:  # если есть - возвращаем страницу с соответствующим сообщением
            context = {'city': data['name']}
            return render(request, 'result_page_city_fail.html', context)
        else:  # если нет - добавляем новый город в базу и выводим отчет
            city = Cities.objects.create(**data)
            context = {'city': city}
            return render(request, 'result_page_city.html', context)

    data = raw_data.errors
    return HttpResponse('{0}'.format(data))


def street_form(request):  # рендер страницы с POST запросом для добавления улицы
    cities = Cities.objects.filter()
    context = {'street_form': StreetForm(), 'cities': cities}
    return render(request, 'street_form.html', context)


def street_form_post(request):  # обработка POST запроса из формы добавления улицы
    raw_data = StreetForm(request.POST)
    if raw_data.is_valid():
        data = raw_data.cleaned_data

        city_name = request.POST.get('city_name')  # получение название города из select
        city = Cities.objects.get(name=city_name)  # получение объекта города из базы по имени city_name

        street = Streets.objects.create(city_id=city.id, **data)  # запись улицы в базу
        context = {'city_name': city.name, 'street': street}  # формирование контекста для страницы результата
        return render(request, 'result_page.html', context)
    data = raw_data.errors
    return HttpResponse('{0}'.format(data))


def search_form2(request):  # рендер страницы с POST запросом для поиска
    context = {'search_form': SearchForm()}
    return render(request, 'search_form2.html', context)


def search_form_post2(request):  # обработка POST запроса из формы поиска
    raw_data = SearchForm(request.POST)
    if raw_data.is_valid():
        data = raw_data.cleaned_data

        streets = Streets.objects.filter(city_id__name=data['city_name_search'])  # получаем все улицы в указанном в форме городе
        if streets:  # если запрос что-то вернул, значит город в базе есть, продолжаем выполнение
            for street in streets:  # обходим каждую улицу
                if street.name == data['street_name_search']:  # если имя улицы равно имени улицы в запросе - выводим её длинну
                    context = {'street': street, 'city': data['city_name_search']}
                    return render(request, 'result_page_street_length.html', context)
            # если не нашлось улицы с совподающим названием, значит такой улицы у города нет, выводим соответствующее сообщение
            context = {'city': data['city_name_search'], 'street': data['street_name_search'], 'message': 'There is no'}
            return render(request, 'result_page_street_length_fail.html', context)
        else:  # если запрос ничего не вернул, значит такого города в базе нет, выводим соответствующее сообщение
            context = {'message': 'There is no', 'street': data['city_name_search'], 'city': 'DB'}
            return render(request, 'result_page_street_length_fail.html', context)

    data = raw_data.errors
    return HttpResponse('{0}'.format(data))
