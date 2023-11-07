# Generated by Django 4.0.4 on 2023-11-07 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('ville', models.CharField(max_length=30)),
                ('code_postal', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=20)),
                ('pays', models.CharField(max_length=20)),
                ('quantite', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('avis', models.CharField(max_length=200)),
            ],
        ),
    ]
