from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import EmprestimoViewSet, formularioEmprestimo, verificaEmprestimo

router = SimpleRouter()
router.register('emprestimos', EmprestimoViewSet) #utilizamos o simple router para poder utilizar
                                                  #de um 'Swagger' mais completo, englobando todas as rotas
                                                  #e métodos.

urlpatterns = [
    path('', formularioEmprestimo, name='formularioEmprestimo'),
    path('verificaEmprestimo', verificaEmprestimo, name='verificaContratos')
]