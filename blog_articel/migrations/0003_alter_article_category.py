# Generated by Django 3.2.8 on 2021-10-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_category', '0002_alter_category_position'),
        ('blog_articel', '0002_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='category_rel_name', to='blog_category.Category'),
        ),
    ]