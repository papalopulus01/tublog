# Generated by Django 4.0.5 on 2022-06-23 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_fecha_publicacion_post_fecha_post_hora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(default='Sin categoría', max_length=255),
        ),
    ]
