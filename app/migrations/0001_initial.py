# Generated by Django 3.2.2 on 2021-05-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('cep', models.FloatField()),
                ('uf', models.CharField(max_length=150)),
                ('cidade', models.CharField(max_length=150)),
                ('logradouro', models.CharField(max_length=150)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=150)),
            ],
        ),
    ]