# Generated by Django 2.2.24 on 2021-11-02 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='recruitment_type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_gender',
            field=models.CharField(choices=[('1', '女性'), ('2', '男性')], default=1, max_length=2, verbose_name='性別'),
        ),
    ]
