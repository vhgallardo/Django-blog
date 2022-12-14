# Generated by Django 4.1.3 on 2022-11-29 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_post_author_alter_post_category_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250, verbose_name='Correo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Boletín',
                'verbose_name_plural': 'Boletines',
                'ordering': ['created'],
            },
        ),
    ]
