# Generated by Django 2.1.15 on 2021-01-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_opinions_idea_opinion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinions',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
