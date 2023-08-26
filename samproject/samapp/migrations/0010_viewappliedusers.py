# Generated by Django 4.1.5 on 2023-01-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samapp', '0009_wishlistmodel_cid'),
    ]

    operations = [
        migrations.CreateModel(
            name='viewappliedusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=30)),
                ('jobtitle', models.CharField(max_length=30)),
                ('fullname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='samapp/static')),
            ],
        ),
    ]
