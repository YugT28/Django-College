# Generated by Django 5.1 on 2024-08-12 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectionApp', '0004_alter_course_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marks', models.SmallIntegerField()),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='course',
            name='unique_Cid_Bid',
        ),
        migrations.AddField(
            model_name='result',
            name='Cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectionApp.course'),
        ),
        migrations.AddField(
            model_name='result',
            name='Sid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collectionApp.student'),
        ),
        migrations.AddConstraint(
            model_name='result',
            constraint=models.UniqueConstraint(fields=('Cid', 'Sid'), name='unique_Cid_Sid'),
        ),
    ]
