# Generated by Django 2.0.3 on 2018-03-30 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_auto_20180326_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphs',
            name='dash_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='graphs',
            name='dash_name',
            field=models.CharField(default='Dash One', max_length=1000),
        ),
    ]