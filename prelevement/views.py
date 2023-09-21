from django.shortcuts import render, get_object_or_404, redirect
from .models import Prelevement
from .forms import PrelevementForm

def list_prelevements(request):
    prelevements = Prelevement.objects.all()
    return render(request, 'prelevement/list.html', {'prelevements': prelevements})

def create_prelevement(request):
    if request.method == 'POST':
        form = PrelevementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prelevement:list')
    else:
        form = PrelevementForm()
    return render(request, 'prelevement/create.html', {'form': form})

def detail_prelevement(request, prelevement_id):
    prelevement = get_object_or_404(Prelevement, pk=prelevement_id)
    return render(request, 'prelevement/detail.html', {'prelevement': prelevement})

def update_prelevement(request, prelevement_id):
    prelevement = get_object_or_404(Prelevement, pk=prelevement_id)
    if request.method == 'POST':
        form = PrelevementForm(request.POST, instance=prelevement)
        if form.is_valid():
            form.save()
            return redirect('prelevement:list')
    else:
        form = PrelevementForm(instance=prelevement)
    return render(request, 'prelevement/update.html', {'form': form, 'prelevement': prelevement})

def delete_prelevement(request, prelevement_id):
    prelevement = get_object_or_404(Prelevement, pk=prelevement_id)
    if request.method == 'POST':
        prelevement.delete()
        return redirect('prelevement:list')
    return render(request, 'prelevement/delete.html', {'prelevement': prelevement})
