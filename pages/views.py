from django.shortcuts import render, redirect
from .forms import formMedico
from .models import Medico
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

def cadastroMedico(request):
    if request.method == "POST":
        form = formMedico (request.POST,request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = formMedico()

    form = formMedico()
    return render(request, "cadastroMedico.html", {'form': form})

def all(request):
    nome = ''
    nomeComment = ''
    if request.method == "POST":
        form = formMedico(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data['name']

