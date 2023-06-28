# Generated by Django 4.2.1 on 2023-06-28 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('exercicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('series', models.PositiveIntegerField()),
                ('repeticoes', models.PositiveIntegerField()),
                ('carga', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercicio.exercicio')),
            ],
        ),
    ]
