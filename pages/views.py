from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
class CadastroPageView(TemplateView):
    template_name = 'cadastroMedico.html'

class CadastroUsuarioPageView(TemplateView):
    template_name ='cadastroUsuario+.html'

class CadastroUsuario1PageView(TemplateView):
    template_name = 'cadastroUsuario++.html' 

class AgendarPageView(TemplateView):
    template_name = 'agendar.html'

def index(request):
    return render(request, "index.html", {})

def cadastroMedico(request):
    if request.method == "post":
        form = formMedico (request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = formMedico()

    form = formPessoa()
    return render(request, "cadastroMedico.html", {'form': form})

def all(request):
    nome = ''
    nomeComment = ''
    if request.method == "post":
        form = formPessoa(request.POST, request.FILES)
        if form.is_valid():
            nome = form.cleaned_data['name']