# Generated by Django 5.0.1 on 2024-01-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_member_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True),
        ),
    ]