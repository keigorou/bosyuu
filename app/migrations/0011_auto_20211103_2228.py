# Generated by Django 2.2.24 on 2021-11-03 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20211103_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.StoreList'),
        ),
    ]