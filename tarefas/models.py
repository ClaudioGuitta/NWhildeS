from django.db import models
from django.contrib.auth.models import User



class Tarefa(models.Model):
    titulo = models.CharField(verbose_name="Titulo",max_length=30)
    usuario = models.ForeignKey(User,on_delete=models.PROTECT)
    data_vencimento = models.DateField(verbose_name="Vencimento")
    descricao = models.TextField(verbose_name="Descrição")
    concluido = models.BooleanField(default=False)
    vencido = models.BooleanField(default=False)
