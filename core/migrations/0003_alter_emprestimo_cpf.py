# Generated by Django 4.2.2 on 2023-06-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_emprestimo_cpf_alter_emprestimo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
    ]