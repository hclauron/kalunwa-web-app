# Generated by Django 4.0.3 on 2022-05-09 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_alter_announcement_options_alter_camppage_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='meta_description',
            field=models.CharField(default='meta description', max_length=225),
            preserve_default=False,
        ),
    ]
