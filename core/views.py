from .models import Emprestimo
from .serializers import EmprestimoSerializer
from rest_framework import viewsets

from django.shortcuts import render
from django.contrib import messages
from .forms import EmprestimoModelForm
from .tasks import verificar_emprestimos

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer


def formularioEmprestimo(request):
    if str(request.method) == 'GET':
        return render(request, 'formularioEmprestimo.html')

def verificaEmprestimo(request): #rota específica para verificar todos os empréstimos pendentes
    if str(request.method) == 'GET':
        verificar_emprestimos.delay()
        return render(request, 'formularioEmprestimo.html')

