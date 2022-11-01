# Generated by Django 4.1.2 on 2022-11-01 16:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('JonsBlog', '0002_post_title_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publication_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]
