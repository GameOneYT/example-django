# Generated by Django 4.2.6 on 2023-12-04 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_count',
            field=models.IntegerField(default=0),
        ),
    ]
