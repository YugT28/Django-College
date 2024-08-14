# Generated by Django 5.1 on 2024-08-11 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiryApp', '0002_stroke'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trauma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquiryApp.enquiry')),
            ],
        ),
    ]
