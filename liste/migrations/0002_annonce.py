# Generated by Django 5.0.6 on 2024-05-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
            ],
        ),
    ]
