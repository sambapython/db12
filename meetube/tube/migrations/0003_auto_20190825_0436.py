# Generated by Django 2.2 on 2019-08-25 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_auto_20190825_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tube.Category'),
        ),
    ]
