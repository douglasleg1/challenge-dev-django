from django import forms
from .models import Emprestimo

class EmprestimoModelForm(forms.ModelForm):

    class Meta:    
        model = Emprestimo
        fields = ['nome', 'cpf', 'endereco', 'valorEmprestimo']
        