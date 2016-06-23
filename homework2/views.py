from django.http import HttpResponse
from django.shortcuts import render
from forms import FirstForm, SecondForm


def first_form(request):
    context = {'first_form': FirstForm()}
    return render(request, 'first_form.html', context)


def second_form(request):
    context = {'second_form': SecondForm()}
    return render(request, 'second_form.html', context)


def first_form_post(request):
    form_data = FirstForm(request.POST)
    if form_data.is_valid():
        data = form_data.cleaned_data
        if data['name'] == 'alex':
            return second_form(request)
        else:
            return HttpResponse('Hello {0}'.format(data['name']))
    data = form_data.errors
    return HttpResponse('Wrong input: {0}'.format(data))


def second_form_post(request):
    form_data = SecondForm(request.POST)
    if form_data.is_valid():
        return HttpResponse('You are registered!')
    data = form_data.errors
    return HttpResponse('Wrong input: {0}'.format(data))
