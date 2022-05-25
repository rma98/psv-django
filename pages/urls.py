from django.urls import path

from . import views 


app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('cadastro', views.CadastroPageView.as_view(), name='cadastro'),
    
]