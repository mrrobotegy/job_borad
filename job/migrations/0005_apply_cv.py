# Generated by Django 3.2.9 on 2021-12-05 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='cv',
            field=models.FileField(default=1, upload_to='apply/'),
            preserve_default=False,
        ),
    ]
