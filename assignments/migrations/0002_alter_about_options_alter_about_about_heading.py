# Generated by Django 5.0.3 on 2024-03-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AlterField(
            model_name='about',
            name='about_heading',
            field=models.CharField(max_length=50),
        ),
    ]
