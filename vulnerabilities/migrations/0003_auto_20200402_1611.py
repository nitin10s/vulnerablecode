# Generated by Django 3.0.3 on 2020-04-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0002_auto_20200402_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisoryhashes',
            name='hash',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
