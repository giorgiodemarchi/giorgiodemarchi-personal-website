# Generated by Django 4.2 on 2023-05-02 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpage',
            options={'ordering': ['-date']},
        ),
    ]
