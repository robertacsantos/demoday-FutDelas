# Generated by Django 2.2.4 on 2019-08-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionalidades', '0007_auto_20190804_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='descricao',
        ),
        migrations.AddField(
            model_name='partida',
            name='local',
            field=models.TextField(default=0, verbose_name='Local da sua partida'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partida',
            name='titulo',
            field=models.CharField(max_length=255, unique=True, verbose_name='Nome de partida'),
        ),
    ]