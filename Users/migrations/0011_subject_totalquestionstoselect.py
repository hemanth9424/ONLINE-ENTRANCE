# Generated by Django 4.1.5 on 2023-06-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_alter_subject_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='TotalQuestionsToSelect',
            field=models.SmallIntegerField(default=1),
        ),
    ]
