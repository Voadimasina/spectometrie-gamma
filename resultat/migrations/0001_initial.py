# Generated by Django 4.2.5 on 2023-10-20 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('etalon', '0001_initial'),
        ('prelevement', '0001_initial'),
        ('bruit_de_fond', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activite', models.FloatField(blank=True, null=True)),
                ('incertitude_activite', models.FloatField(blank=True, null=True)),
                ('teneur', models.FloatField(blank=True, null=True)),
                ('bruit_de_fond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bruit_de_fond.bruitdefond')),
                ('etalon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etalon.etalon')),
                ('prelevement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prelevement.prelevement')),
            ],
        ),
    ]