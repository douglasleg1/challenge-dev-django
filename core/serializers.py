from rest_framework import serializers
from .models import Emprestimo
class EmprestimoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emprestimo
        fields = (
            'id',
            'criado', 
            'modificação', 
            'status', 
            'nome', 
            'endereco',
            'valorEmprestimo',
            'slug',
            'cpf'
        )
