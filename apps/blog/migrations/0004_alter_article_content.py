# Generated by Django 3.2.4 on 2021-06-11 14:45

from django.db import migrations
import django_editorjs_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_editorjs_fields.fields.EditorJsTextField(blank=True, null=True),
        ),
    ]
