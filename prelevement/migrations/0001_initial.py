# Generated by Django 4.2.5 on 2023-09-21 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prelevement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temps_de_comptage', models.DateTimeField()),
                ('aire_nette', models.FloatField()),
                ('incertitude_aire_nette', models.FloatField()),
                ('taux_de_comptage', models.FloatField()),
                ('incertitude_taux_de_comptage', models.FloatField()),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.produit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
