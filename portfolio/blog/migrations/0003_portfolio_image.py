# Generated by Django 3.0.8 on 2020-08-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_portfolio_tel'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/pics'),
        ),
    ]
