# Generated by Django 3.2.4 on 2021-06-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='placeholder.jpg', upload_to='img'),
            preserve_default=False,
        ),
    ]
