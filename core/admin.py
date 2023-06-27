from django.contrib import admin
from .models import Emprestimo
# Register your models here.


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'valorEmprestimo', 'status', 'criado')