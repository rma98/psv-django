from django.contrib import admin
from django.urls import include
from django.urls import path





urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls', namespace='pages')),
    path('cadastro', include('pages.urls', namespace='pages')),
    
]
