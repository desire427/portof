from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PortofolioForm


def home(request):
    if request.method == "POST":
        form = PortofolioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PortofolioForm()
    return render(request, "index.html", {"form": form})

def portfoliofomulaire(request):
    if request.method == 'POST':
        form = PortofolioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PortofolioForm()
    return render(request, 'contact.html', {'form': form})