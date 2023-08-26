# Generated by Django 4.1.5 on 2023-01-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samapp', '0007_jobapplymodel_jobtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlistmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('jobtitle', models.CharField(max_length=35)),
                ('jobtype', models.CharField(max_length=50)),
                ('worktype', models.CharField(max_length=30)),
                ('experiencerequired', models.CharField(max_length=20)),
                ('qualificationrequired', models.CharField(max_length=100)),
            ],
        ),
    ]
