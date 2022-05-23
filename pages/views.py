from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

def cadastro(request):
    if request.method == "POST":
        form = formMedico (request.POST,request.FILES)