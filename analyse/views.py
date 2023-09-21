from django.shortcuts import render, get_object_or_404, redirect
from .models import Analyse
from .forms import AnalyseForm

def list_analyses(request):
    analyses = Analyse.objects.all()
    return render(request, 'analyse/list.html', {'analyses': analyses})

def create_analyse(request):
    if request.method == 'POST':
        form = AnalyseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('analyse:list')
    else:
        form = AnalyseForm()
    return render(request, 'analyse/create.html', {'form': form})

def detail_analyse(request, analyse_id):
    analyse = get_object_or_404(Analyse, pk=analyse_id)
    return render(request, 'analyse/detail.html', {'analyse': analyse})

def update_analyse(request, analyse_id):
    analyse = get_object_or_404(Analyse, pk=analyse_id)
    if request.method == 'POST':
        form = AnalyseForm(request.POST, instance=analyse)
        if form.is_valid():
            form.save()
            return redirect('analyse:list')
    else:
        form = AnalyseForm(instance=analyse)
    return render(request, 'analyse/update.html', {'form': form, 'analyse': analyse})

def delete_analyse(request, analyse_id):
    analyse = get_object_or_404(Analyse, pk=analyse_id)
    if request.method == 'POST':
        analyse.delete()
        return redirect('analyse:list')
    return render(request, 'analyse/delete.html', {'analyse': analyse})
