# Generated by Django 4.2.5 on 2023-09-22 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bruit_de_fond', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bruitdefond',
            name='incertitude_taux_de_comptage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bruitdefond',
            name='taux_de_comptage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
