# Generated by Django 5.0.7 on 2024-07-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qdelivery', '0015_alter_produtos_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='tipo',
            field=models.CharField(choices=[('Q', 'Quentinha'), ('B', 'Bebidas')], max_length=1),
        ),
    ]
