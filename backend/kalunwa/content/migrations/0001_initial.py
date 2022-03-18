# Generated by Django 4.0.3 on 2022-03-18 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=225)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/content/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('name', models.CharField(db_index=True, max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('camp', models.CharField(choices=[('SB', 'Suba'), ('LSNG', 'Lasang'), ('BYBYN', 'Baybayon'), ('ZW', 'Zero Waste'), ('GNRL', 'General')], default='GNRL', max_length=5)),
                ('is_featured', models.BooleanField(default=False)),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='content.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(default=' ')),
                ('image', models.OneToOneField(default=' ', on_delete=django.db.models.deletion.PROTECT, related_name='news', to='content.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jumbotron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('header_title', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=225)),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='jumbotrons', to='content.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='content.tag'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('camp', models.CharField(choices=[('SB', 'Suba'), ('LSNG', 'Lasang'), ('BYBYN', 'Baybayon'), ('ZW', 'Zero Waste'), ('GNRL', 'General')], default='GNRL', max_length=5)),
                ('is_featured', models.BooleanField(default=False)),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='content.image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
