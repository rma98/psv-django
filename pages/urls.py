from django.urls import path

from . import views 


app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('cadastro', views.CadastroPageView.as_view(), name='cadastro'),
    path('cadastro_usuario', views.CadastroUsuarioPageView.as_view(), name='cadastro_usuario'),
    path('cadastro_usuario_', views.CadastroUsuario1PageView.as_view(), name='cadastro_usuario_'),
    
]