# Generated by Django 5.0.3 on 2024-03-31 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_rename_updayed_at_category_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_body',
            field=models.TextField(max_length=10000),
        ),
    ]
