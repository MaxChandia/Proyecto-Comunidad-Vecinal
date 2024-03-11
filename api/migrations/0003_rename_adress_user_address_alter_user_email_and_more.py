# Generated by Django 5.0.3 on 2024-03-11 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_user_register_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='adress',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rut',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]