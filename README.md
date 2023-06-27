## AGRADECIMENTOS
<p> Desde já agradeço a participação no processo seletivo, foi uma experiência muito enriquecedora.
    Possui alguns contratempos com prazos e dificuldades com Containers Docker, porém gravei um vídeo
    de tudo funcionando localmente que estará na raiz do projeto.</p>

## COMO RODAR O PROJETO LOCALMENTE (com o rabbitmq-server previamente instalado)
- rabbitmq-server
- python3 -m venv [nome_da_sua_virtual_env]
- source [nome_da_sua_virtual_env]/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt
- Abrir três abas no terminal
- <b> Primeira aba </b> na raíz do projeto: python3 manage.py runserver
- <b> Segunda aba </b> na raíz do projeto: celery -A emprestimosproject worker -l INFO
- <b> Terceira aba </b> na raíz do projeto: python3 manage.py shell
- <b> Terceira aba </b> from core.tasks import verificar_emprestimos
- <b> Terceira aba - sempre que quiser rodar o celery manualmente </b> a = verificar_emprestimos.delay()

## COMO RODAR O PROJETO DOCKER
<p> O emprestimosproject.settings estava configurado para rodar localmente, alterar o CELERY_BROKER_URL para
    'amqp://guest:guest@celery_broker:5672//'</p>
- python3 -m venv [nome_da_sua_virtual_env]
- source [nome_da_sua_virtual_env]/bin/activate
- docker compose up -d

## Autenticação do DJANGO ADMIN
- route for admin django: http://localhost:8000/admin/
- login: root
- password: root321

## ROTAS AUXILIARES DJANGO REST FRAMEWORK
<p> O DRF está com o permissionamento para 'IsAuthenticatedOrReadOnly', portanto para restar métodos de POST,
PATCH, PUT ou DELETE, deve-se realizar a autenticação com os dados informados acima.

- localhost:8000/api/v1/emprestimos/ (Para listar todos os empréstimos registrados)
- localhost:8000/api/v1/emprestimos/<int:id> (para visualizar um empréstimo específico)
- localhost:8000/admin/
- localhost:8000/verificaEmprestimos/ (Para aprovar ou reprovar os empréstimos manualmente)