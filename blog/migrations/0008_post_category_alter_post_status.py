# Generated by Django 4.0.1 on 2022-02-01 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blog.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Moi', 'moi'), ('Monde', 'monde')], default='moi', max_length=5),
        ),
    ]
