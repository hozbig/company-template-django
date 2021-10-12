# Generated by Django 3.2.8 on 2021-10-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='articles-image/')),
                ('time_for_read', models.IntegerField(default=5)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('publish_time', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('p', 'publish'), ('d', 'draft')], default='p', max_length=1)),
                ('suggest', models.BooleanField(default=False, help_text='If true: avaibale to show in suggest field.')),
            ],
        ),
    ]
