from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include
urlpatterns = [
    path('', auth_views.LoginView.as_view(
    template_name='usuarios/login.html',
    extra_context={'titulo': 'Autenticação do Condômino'}
), name='login'),
    
    path('usuarios/', include('django.contrib.auth.urls')),
]