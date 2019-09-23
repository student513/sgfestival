# Generated by Django 2.1.3 on 2019-09-23 12:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foodtruck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftName', models.CharField(blank=True, max_length=100)),
                ('ftImage', models.ImageField(blank=True, upload_to='images/')),
                ('ftCategory', models.CharField(choices=[('korean', '한식'), ('western', '양식'), ('dessert', '디저트'), ('etc', '기타')], default='', max_length=100)),
                ('generalRating', models.FloatField(default='0.0', max_length=10)),
                ('ftMenu1', models.CharField(blank=True, max_length=100)),
                ('ftMenu2', models.CharField(blank=True, max_length=100)),
                ('ftMenu3', models.CharField(blank=True, max_length=100)),
                ('ftMenu4', models.CharField(blank=True, max_length=100)),
                ('ftMenu5', models.CharField(blank=True, max_length=100)),
                ('ftMenu6', models.CharField(blank=True, max_length=100)),
                ('ftMenu7', models.CharField(blank=True, max_length=100)),
                ('ftMenu8', models.CharField(blank=True, max_length=100)),
                ('ftMenu9', models.CharField(blank=True, max_length=100)),
                ('ftMenu10', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoodtruckComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftRating', models.FloatField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], default='5', max_length=10)),
                ('ftCommentImage', models.ImageField(blank=True, upload_to='images/')),
                ('ftComment', models.CharField(blank=True, max_length=300)),
                ('ftCommentAuthor', models.CharField(default='Anonymous', max_length=100)),
                ('ftCommentTimeStamp', models.DateTimeField(default=datetime.datetime(2019, 9, 23, 12, 40, 8, 359952, tzinfo=utc))),
                ('foodtruck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodtruck.Foodtruck')),
            ],
            options={
                'ordering': ('-ftCommentTimeStamp',),
            },
        ),
    ]
