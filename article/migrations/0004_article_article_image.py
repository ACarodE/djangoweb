# Generated by Django 2.1.2 on 2018-10-30 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_remove_article_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Resim Ekle'),
        ),
    ]
