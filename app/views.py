from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    comment = request.POST.get('comment')
    comment = comment.split()
    data_list = []
    for word in comment:
        data = {}
        data['name'] = word
        data['length'] = len(word)
        data_list.append(data)
    context = {'context': data_list}
    return render(request, '1.html', context)


def link_hello_world(request):
    return render(request, 'hello_world.html')


def link_hello_earth(request):
    return render(request, 'hello_earth.html')


def link_hello_universe(request):
    return render(request, 'hello_universe.html')
