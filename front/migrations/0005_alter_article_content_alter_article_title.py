# Generated by Django 4.1.5 on 2023-03-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("front", "0004_article_articledescription_alter_article_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(db_column="CONTENT", max_length=5000),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(db_column="TITLE", max_length=50),
        ),
    ]
