# Generated by Django 4.1.5 on 2023-03-04 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientemail",
            name="email",
            field=models.CharField(db_column="EMAIL", max_length=50, unique=True),
        ),
    ]
