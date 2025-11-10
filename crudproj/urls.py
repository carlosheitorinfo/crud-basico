from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Função personalizada para permitir logout via GET
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')  # Redireciona para a página inicial após o logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projetos.urls')),
    path('logout/', logout_view, name='logout'),  # Substitui a rota de logout para aceitar GET
]
