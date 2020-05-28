from django.urls import path
from .views import *

#o padrão para os nomes que estou usando é simples:
#Duas letras da ação e duas letras da classe alvo
#Exemplo: CrTa = criar tarefa

urlpatterns = [
    path('criartarefa/', createTarefa, name='CrTa'),
    path('listatarefa/', listTarefa, name='LiTa'),
    path('concluitarefa/<int:id>', marcaConcluido, name='marcaConcluido'),
    path('tarefa/<int:id>', verTarefa, name='VeTa'),
    path('atualizartarefa/<int:id>/', updateTarefa, name='UpTa'),

]