# Generated by Django 4.1.6 on 2023-02-02 18:18

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
