# coding: UTF-8
from django.shortcuts import render, redirect
from models import Equipments, Workers
from forms import WorkerForm, EquipmentForm


# заглавная страница
def index(request):
    return render(request, 'homework5_index.html')


# страница с таблицей работников
def view_workers(request):
    workers = Workers.objects.filter()
    context = {'workers': workers}
    return render(request, 'homework5_view_workers.html', context)


# форма добавления нового работника
def add_worker(request):
    if request.method == 'POST':
        raw_data = WorkerForm(request.POST)
        if raw_data.is_valid():
            data = raw_data.cleaned_data
            worker = Workers.objects.create(**data)  # запись работника в базу
            request.session['worker_id'] = worker.id  # добавление в сессию id работника чтобы в форме добавления инструмента привязать инструмент к этому работнику
            return redirect(add_equipment)  # редиректим на форму добавления инструмента
        context = {'worker_form': raw_data}
        return render(request, 'homework5_add_worker.html', context)
    else:
        context = {'worker_form': WorkerForm()}
        return render(request, 'homework5_add_worker.html', context)


# страница с таблицей инструмента
def view_equipment(request):
    equipments = Equipments.objects.filter()
    context = {'equipments': equipments}
    return render(request, 'homework5_view_equipment.html', context)


# форма добавления инструмента при переходе из страницы инструмента
def add_equipment2(request):
    if request.method == 'POST':

        owner_id = request.POST.get('owner')  # получение id работника из формы
        owner = Workers.objects.get(id=owner_id)  # получение объекта работника из базы

        raw_data = EquipmentForm(request.POST)
        if raw_data.is_valid():
            data = raw_data.cleaned_data
            Equipments.objects.create(equipment_owner_id=owner.id, **data)
            return redirect(view_equipment)  # редирект на странику с таблицей инструмента
        context = {'equipment_form': raw_data}
        return render(request, 'homework5_view_equipment.html', context)
    else:
        workers = Workers.objects.filter()
        context = {'equipment_form': EquipmentForm(), 'workers': workers}
        return render(request, 'homework5_add_equipment2.html', context)


# форма добавления инструмента при переходе из страницы работников
def add_equipment(request):
    if request.method == 'POST':

        worker_id = request.session.get('worker_id')  # получение id работника из сессии
        worker = Workers.objects.get(id=worker_id)  # получение объекта работника из базы

        raw_data = EquipmentForm(request.POST)
        if raw_data.is_valid():
            data = raw_data.cleaned_data
            Equipments.objects.create(equipment_owner_id=worker.id, **data)
            return redirect(add_equipment)  # редирект на страницу с таблицей инструмента, можно добавить ещё одного инструмент для данного работника, или вернуться на первую страницу
        context = {'equipment_form': raw_data}
        return render(request, 'homework5_add_equipment.html', context)
    else:
        context = {'equipment_form': EquipmentForm()}
        return render(request, 'homework5_add_equipment.html', context)
