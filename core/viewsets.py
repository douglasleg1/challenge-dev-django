from rest_framework.viewsets import ModelViewSet
from .serializers import EmprestimoSerializer
from .models import Emprestimo
from .tasks import verificar_emprestimos
class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def perform_create(self, serializer):
        emprestimo = serializer.save()
        verifica_emprestimos = verificar_emprestimos.delay()
