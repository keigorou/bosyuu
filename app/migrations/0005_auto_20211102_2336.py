# Generated by Django 2.2.24 on 2021-11-02 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211102_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Recruit'),
        ),
    ]
