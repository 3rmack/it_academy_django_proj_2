from django.shortcuts import render, redirect
from models import Equipments, Workers
from forms import WorkerForm, EquipmentForm


def index(request):
    return render(request, 'homework5_index.html')


def view_workers(request):
    workers = Workers.objects.filter()
    context = {'workers': workers}
    return render(request, 'homework5_view_workers.html', context)


def add_worker(request):
    if request.method == 'POST':
        raw_data = WorkerForm(request.POST)
        if raw_data.is_valid():
            data = raw_data.cleaned_data
            worker = Workers.objects.create(**data)
            request.session['worker_id'] = worker.id
            return redirect(add_equipment)
            # return add_equipment_form(request, worker)
        context = {'worker_form': raw_data}
        return render(request, 'homework5_add_worker.html', context)
    else:
        context = {'worker_form': WorkerForm()}
        return render(request, 'homework5_add_worker.html', context)



def view_equipment(request):
    pass


# def add_equipment_form(request):
#     context = {'equipment_form': EquipmentForm(), 'worker_id': worker.id}
#     return render(request, 'homework5_add_equipment.html', context)


def add_equipment(request):
    # worker_id = request.POST.get('worker_id')
    # worker = Workers.objects.get(id=worker_id)
    if request.method == 'POST':

        worker_id = request.session.get('worker_id')
        del request.session['worker_id']
        worker = Workers.objects.get(id=worker_id)

        raw_data = EquipmentForm(request.POST)
        if raw_data.is_valid():
            data = raw_data.cleaned_data
            Equipments.objects.create(equipment_owner_id=worker.id, **data)
            return index(request)
        context = {'equipment_form': raw_data}
        return render(request, 'homework5_add_equipment.html', context)
    else:
        context = {'equipment_form': EquipmentForm()}
        return render(request, 'homework5_add_equipment.html', context)
