# Generated by Django 3.0.4 on 2020-04-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200413_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='user_bio',
            field=models.TextField(default='Здесь еще нчиего нет! Расскажите о себе'),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='user_photo',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2F%25D0%2590%25D0%25BD%25D0%25BE%25D0%25BD%25D0%25B8%25D0%25BC&psig=AOvVaw1GtxM-KqD3znJTWT8YfIC5&ust=1586882803726000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOinxp_t5egCFQAAAAAdAAAAABAD', max_length=2000),
        ),
    ]