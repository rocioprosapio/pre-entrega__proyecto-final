# Generated by Django 4.1.3 on 2023-01-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes_blog', '0004_mensaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=3000)),
            ],
        ),
    ]
