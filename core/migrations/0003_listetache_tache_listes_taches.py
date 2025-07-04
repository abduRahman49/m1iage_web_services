# Generated by Django 5.2.1 on 2025-06-14 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_categorie_tache_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeTache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='tache',
            name='listes_taches',
            field=models.ManyToManyField(to='core.listetache'),
        ),
    ]
