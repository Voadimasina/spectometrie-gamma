from django.shortcuts import render, get_object_or_404, redirect
from .models import BruitDeFond
from .forms import BruitDeFondForm  # Vous devrez créer ce formulaire

def list_bruitdefond(request):
    bruitdefond = BruitDeFond.objects.all()
    return render(request, 'bruitdefond/list.html', {'bruitdefond': bruitdefond})

def create_bruitdefond(request):
    if request.method == 'POST':
        form = BruitDeFondForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bruitdefond:list')
    else:
        form = BruitDeFondForm()
    return render(request, 'bruitdefond/create.html', {'form': form})

def detail_bruitdefond(request, bruitdefond_id):
    bruitdefond = get_object_or_404(BruitDeFond, pk=bruitdefond_id)
    return render(request, 'bruitdefond/detail.html', {'bruitdefond': bruitdefond})

def update_bruitdefond(request, bruitdefond_id):
    bruitdefond = get_object_or_404(BruitDeFond, pk=bruitdefond_id)
    if request.method == 'POST':
        form = BruitDeFondForm(request.POST, instance=bruitdefond)
        if form.is_valid():
            form.save()
            return redirect('bruitdefond:list')
    else:
        form = BruitDeFondForm(instance=bruitdefond)
    return render(request, 'bruitdefond/update.html', {'form': form, 'bruitdefond': bruitdefond})

def delete_bruitdefond(request, bruitdefond_id):
    bruitdefond = get_object_or_404(BruitDeFond, pk=bruitdefond_id)
    if request.method == 'POST':
        bruitdefond.delete()
        return redirect('bruitdefond:list')
    return render(request, 'bruitdefond/delete.html', {'bruitdefond': bruitdefond})
