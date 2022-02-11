# Generated by Django 4.0.1 on 2022-02-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_date_published_alter_post_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Monde', 'monde'), ('Moi', 'moi')], default='moi', max_length=5),
        ),
    ]
