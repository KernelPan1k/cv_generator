# Generated by Django 3.0.6 on 2020-11-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20200507_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='language',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Language'),
        ),
    ]
