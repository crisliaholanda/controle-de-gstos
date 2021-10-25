from django.shortcuts import redirect, render
from .models import Categoria, Transacao
from .forms import TransacaoForm
import datetime

def home(request):
    return render(request, 'contas/home.html')

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form
    return render(request, 'contas/nova_transacao.html', data)

def update_transacao(request, pkid):
    data = {}
    transacao = Transacao.objects.get(pk=pkid)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('listagem')

    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/update_transacao.html', data)

def delete_transacao(request, pkid):
    transacao = Transacao.objects.get(pk=pkid)
    transacao.delete()
    return redirect('listagem')