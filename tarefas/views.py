from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from datetime import date, timedelta, datetime



@login_required(login_url='login')
def createTarefa(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        #Aqui nós salvaremos o usuario da tarefa como aquele logado...
        tarefa = form.save(commit=False)
        tarefa.usuario = request.user
        tarefa.save()
        return redirect('LiTa')

    return render(request, 'createTarefa.html',{'form':form})

@login_required(login_url='login')
def listTarefa(request):

    tarefas = Tarefa.objects.filter(usuario = request.user).order_by('data_vencimento')
    tarefas_vencidas = []
    tarefas_concluidas=[]
    tarefas_abertas = []
    for tarefa in tarefas:
        if tarefa.concluido:
            tarefas_concluidas.append(tarefa)
        else:

            if date.today() > tarefa.data_vencimento:
                tarefas_vencidas.append(tarefa)
            else:
                tarefas_abertas.append(tarefa)


    return render(request, 'listaTarefas.html', {'tarefas_abertas':tarefas_abertas,'tarefas_vencidas':tarefas_vencidas,
                                                 'tarefas_concluidas':tarefas_concluidas})


def verTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    return render(request, 'verTarefa.html', {'tarefa':tarefa})

def updateTarefa(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    form = TarefaForm(request.POST or None, instance= tarefa)
    if form.is_valid():
        form.save()
        return redirect('VeTa', id=id)

    return render(request, 'updateTarefa.html', {'form':form})



def marcaConcluido(request, id):
    tarefa = get_object_or_404(Tarefa, pk=id)
    form = TarefaForm(request.POST or None, instance=tarefa)
    tarefa= form.save(commit=False)
    tarefa.concluido = True
    tarefa.save()
    return redirect('LiTa')
