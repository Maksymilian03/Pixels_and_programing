# Generated by Django 4.1 on 2023-06-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='jpg',
            field=models.ImageField(blank=True, null=True, upload_to='blog/static/jpg'),
        ),
    ]
