from __future__ import absolute_import, unicode_literals
from emprestimosproject import app
from .models import Emprestimo
import logging

@app.task
def verificar_emprestimos():
    logging.warning('Iniciando avaliação do Empréstimo!')
    try:
        emprestimos = Emprestimo.objects.all() #recebemos todos os empréstimos 

        for emprestimo in emprestimos:
            if emprestimo.status != 0: # condição para rodar apenas o status 0: "EM ANÁLISE"
                if emprestimo.id % 2 ==0: # se o id do empréstimo por par será aprovado
                    emprestimo.status = 1
                else: #caso contrário reprovamos
                    emprestimo.status = 2
                print(f'CPF:{emprestimo.cpf} | STATUS: {emprestimo.status}') #exibimos dentro do celery
                emprestimo.save()

    except Exception as err:
        logging.error(f'Erro ao processar o empréstimo: {err}')
        raise err
    finally:
        logging.warning('Avaliação do empréstimo finalizada!')
