# Generated by Django 4.1.5 on 2023-03-08 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0002_alter_clientemail_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="article",
            name="creationDate",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
