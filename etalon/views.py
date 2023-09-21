from django.shortcuts import render, get_object_or_404, redirect
from .models import Etalon
from .forms import EtalonForm

def list_etalons(request):
    etalons = Etalon.objects.all()
    return render(request, 'etalon/list.html', {'etalons': etalons})

def create_etalon(request):
    if request.method == 'POST':
        form = EtalonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('etalon:list')
    else:
        form = EtalonForm()
    return render(request, 'etalon/create.html', {'form': form})

def detail_etalon(request, etalon_id):
    etalon = get_object_or_404(Etalon, pk=etalon_id)
    return render(request, 'etalon/detail.html', {'etalon': etalon})

def update_etalon(request, etalon_id):
    etalon = get_object_or_404(Etalon, pk=etalon_id)
    if request.method == 'POST':
        form = EtalonForm(request.POST, instance=etalon)
        if form.is_valid():
            form.save()
            return redirect('etalon:list')
    else:
        form = EtalonForm(instance=etalon)
    return render(request, 'etalon/update.html', {'form': form, 'etalon': etalon})

def delete_etalon(request, etalon_id):
    etalon = get_object_or_404(Etalon, pk=etalon_id)
    if request.method == 'POST':
        etalon.delete()
        return redirect('etalon:list')
    return render(request, 'etalon/delete.html', {'etalon': etalon})
