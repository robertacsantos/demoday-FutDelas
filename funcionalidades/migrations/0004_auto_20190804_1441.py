# Generated by Django 2.2.3 on 2019-08-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionalidades', '0003_auto_20190804_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='senha',
            field=models.CharField(default=' ', max_length=255, verbose_name='senha'),
            preserve_default=False,
        ),
    ]
