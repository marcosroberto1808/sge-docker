# Generated by Django 2.0.2 on 2018-02-27 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal', '0002_estagiario_sexo'),
        ('organizacional', '0002_auto_20180227_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatorioEstagiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estagiario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pessoal.Estagiario', verbose_name='Estagiário')),
            ],
        ),
        migrations.AlterModelOptions(
            name='unidadefederativa',
            options={'verbose_name': 'Unidade Federativa', 'verbose_name_plural': 'Unidades Federativas'},
        ),
    ]
