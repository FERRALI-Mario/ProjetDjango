# Generated by Django 4.0.1 on 2022-02-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_category_alter_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
