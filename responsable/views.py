from django.shortcuts import render, get_object_or_404, redirect
from .models import Responsable
from .forms import ResponsableForm

def list_responsables(request):
    responsables = Responsable.objects.all()
    return render(request, 'responsable/list.html', {'responsables': responsables})

def create_responsable(request):
    if request.method == 'POST':
        form = ResponsableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('responsable:list')
    else:
        form = ResponsableForm()
    return render(request, 'responsable/create.html', {'form': form})

def detail_responsable(request, responsable_id):
    responsable = get_object_or_404(Responsable, pk=responsable_id)
    return render(request, 'responsable/detail.html', {'responsable': responsable})

def update_responsable(request, responsable_id):
    responsable = get_object_or_404(Responsable, pk=responsable_id)
    if request.method == 'POST':
        form = ResponsableForm(request.POST, instance=responsable)
        if form.is_valid():
            form.save()
            return redirect('responsable:list')
    else:
        form = ResponsableForm(instance=responsable)
    return render(request, 'responsable/update.html', {'form': form, 'responsable': responsable})

def delete_responsable(request, responsable_id):
    responsable = get_object_or_404(Responsable, pk=responsable_id)
    if request.method == 'POST':
        responsable.delete()
        return redirect('responsable:list')
    return render(request, 'responsable/delete.html', {'responsable': responsable})
