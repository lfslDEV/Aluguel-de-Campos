from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),  # url para a autenticação de usuários
    path('', include('core.urls')), # url para o app core
]
