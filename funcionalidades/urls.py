from django.urls import path, include
from funcionalidades.views import index, sobre, login, cadastrar_partida, home, remover_partida
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home),
    path('index', index),
    path('sobre', sobre),
    path('login', login),
    path('partidas', cadastrar_partida),
    path('remover_partida/<int:id>/', remover_partida),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# tag para configurar os arquivos staticos