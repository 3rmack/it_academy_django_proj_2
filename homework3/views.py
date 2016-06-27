# coding: UTF-8
from django.shortcuts import render
from django.http import HttpResponse
from forms import DataForm, SearchForm
from models import DataFormModel


def index(request):
    return render(request, 'first_page.html')


def data_form(request):
    context = {'data_form': DataForm()}
    return render(request, 'data_form.html', context)


def search_form(request):
    context = {'search_form': SearchForm()}
    return render(request, 'search_form.html', context)


def data_form_post(request):
    data_from_form = DataForm(request.POST)
    if data_from_form.is_valid():
        data = data_from_form.cleaned_data
        DataFormModel.objects.create(**data)
        return index(request)
    data = data_from_form.errors
    return HttpResponse('Wrong input: {0}'.format(data))


def search_in_db(search_request_from_form):  # функция поиска в базе
    search_request = {}  # список фильтра запроса
    #  дальше обратаывается каждый элемент словаря, полученного на вход функции из формы
    #  если элемент не заполнен - то игнорируется, если заполнен - добавляется в фильтр запроса
    if search_request_from_form['name'] != '':
        search_request['name'] = search_request_from_form['name']
    if search_request_from_form['favourite_color'] != '':
        search_request['favourite_color'] = search_request_from_form['favourite_color']
    if search_request_from_form['email'] != '':
        search_request['email'] = search_request_from_form['email']
    if search_request_from_form['height'] is not None:
        search_request['height'] = search_request_from_form['height']
    if search_request_from_form['weight'] is not None:
        search_request['weight'] = search_request_from_form['weight']
    return DataFormModel.objects.filter(**search_request)


def search_form_post(request):  # функция получения POST запроса на поиск в базе и вывод результата
    data_from_form = SearchForm(request.POST)  # получение POST запроса
    if data_from_form.is_valid():  # валидация данных
        data = data_from_form.cleaned_data
        result = search_in_db(data)  # вызов функции поиска в базе
        context = {'context': result}  # словарь для формирования html страницы с ответом
        if len(result) > 0:  # проверка, нашел ли что-то поиск
            return render(request, 'result_table.html', context)  # если нашел - рендерим ответный html
        else:
            return HttpResponse('No data found')  # если пустой результат поиска - выводим сообщение
    data = data_from_form.errors
    return HttpResponse('Wrong input: {0}'.format(data))
