from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit
from .forms import ProduitForm  # Vous devrez créer ce formulaire

def list_produits(request):
    produits = Produit.objects.all()
    return render(request, 'produit/list.html', {'produits': produits})

def create_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produit:list')
    else:
        form = ProduitForm()
    return render(request, 'produit/create.html', {'form': form})

def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    return render(request, 'produit/detail.html', {'produit': produit})

def update_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produit:list')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'produit/update.html', {'form': form, 'produit': produit})

def delete_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    if request.method == 'POST':
        produit.delete()
        return redirect('produit:list')
    return render(request, 'produit/delete.html', {'produit': produit})
