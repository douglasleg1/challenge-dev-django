from django.db import models

# Create your models here.
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificação = models.DateField('Data de Modificação', auto_now=True)
    statusEmprestimos = [(0, 'Em análise'), (1, 'Aprovado'), (2, 'Negado')]
    status = models.IntegerField('Status Empréstimo', choices=statusEmprestimos, default=0)

    class Meta:
        abstract = True

class Emprestimo(Base):
    nome = models.CharField('Nome Completo', max_length=200)
    cpf = models.CharField('CPF', max_length=11)
    endereco = models.CharField('Endereço', max_length=400)
    valorEmprestimo = models.DecimalField('Valor do Empréstimo Pretendido', decimal_places=2, max_digits=8)
    slug = models.SlugField('Slug Nome Cliente', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome
    
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Emprestimo)
