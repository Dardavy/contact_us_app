# Generated by Django 4.2.2 on 2023-07-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=300)),
                ('message', models.TextField(max_length=1000)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
