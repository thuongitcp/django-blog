# Generated by Django 5.0.3 on 2024-03-30 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blog_blog_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='updayed_at',
            new_name='updated_at',
        ),
    ]