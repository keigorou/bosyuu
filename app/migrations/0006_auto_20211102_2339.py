# Generated by Django 2.2.24 on 2021-11-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20211102_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='store',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]