# Generated by Django 4.2.5 on 2023-09-22 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analyse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_du_produit', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('quantite', models.FloatField()),
                ('analyse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyse.analyse')),
            ],
        ),
    ]
