# Generated by Django 4.1.5 on 2023-03-08 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0003_article_category_article_creationdate"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="description",
            field=models.TextField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(db_column="CONTENT", max_length=3000),
        ),
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(upload_to="articleImages/"),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(db_column="TITLE", max_length=40),
        ),
    ]
