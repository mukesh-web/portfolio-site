# Generated by Django 3.0.8 on 2020-08-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_portfolio_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]