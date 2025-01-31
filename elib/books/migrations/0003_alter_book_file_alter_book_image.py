# Generated by Django 5.1.2 on 2024-12-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_full_description_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
