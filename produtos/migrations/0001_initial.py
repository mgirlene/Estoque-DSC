# Generated by Django 3.1.5 on 2021-03-05 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gerenciador', '0001_initial'),
        ('estoques', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_validade', models.DateTimeField(verbose_name='Data de Validade')),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('quantidade', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerenciador.categoria')),
                ('estoque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoques.estoque')),
            ],
            options={
                'db_table': 'produto',
            },
        ),
    ]
