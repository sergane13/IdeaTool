# Generated by Django 2.2.5 on 2020-12-31 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_auto_20201231_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='neutralism_1_grade',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='neutralism_2_grade',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='neutralism_3_grade',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='optimism_1_grade',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='pessimism_1_grade',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='idea',
            name='pessimism_2_grade',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=1, null=True),
        ),
    ]
