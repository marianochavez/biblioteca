# Generated by Django 3.1.7 on 2021-04-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0011_auto_20210326_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='cantidad',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Stock'),
        ),
        migrations.AddField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='libro/', verbose_name='Imagen'),
        ),
    ]
