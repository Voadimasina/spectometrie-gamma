from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm

def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'client/list.html', {'clients': clients})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client:list')
    else:
        form = ClientForm()
    return render(request, 'client/create.html', {'form': form})

def detail_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    return render(request, 'client/detail.html', {'client': client})

def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client:list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/update.html', {'form': form, 'client': client})

def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client:list')
    return render(request, 'client/delete.html', {'client': client})
