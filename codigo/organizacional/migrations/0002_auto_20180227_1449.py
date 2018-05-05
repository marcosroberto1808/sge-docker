# Generated by Django 2.0.2 on 2018-02-27 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizacional', '0001_initial'),
        ('pessoal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefone',
            name='estagiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.Estagiario', verbose_name='Estagiario'),
        ),
        migrations.AddField(
            model_name='telefone',
            name='tipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='organizacional.TipoTelefone', verbose_name='Tipo de Telefone'),
        ),
        migrations.AddField(
            model_name='recesso',
            name='estagiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.Estagiario', verbose_name='Estagiário'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacional.Cidade', verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='estagiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoal.Estagiario', verbose_name='Estagiário'),
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacional.UnidadeFederativa', verbose_name='UF'),
        ),
    ]