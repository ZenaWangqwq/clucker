# Generated by Django 3.2.8 on 2021-10-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblogs', '0006_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
