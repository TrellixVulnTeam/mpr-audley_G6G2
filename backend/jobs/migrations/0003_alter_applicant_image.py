# Generated by Django 3.2.9 on 2022-05-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_applicant_jobsapplied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='applicant_images'),
        ),
    ]
