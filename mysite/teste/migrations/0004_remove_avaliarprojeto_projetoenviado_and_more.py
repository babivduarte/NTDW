# Generated by Django 4.1.7 on 2023-06-15 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0003_remove_enviarprojeto_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliarprojeto',
            name='projetoEnviado',
        ),
        migrations.AddField(
            model_name='avaliarprojeto',
            name='projeto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teste.projeto'),
            preserve_default=False,
        ),
    ]