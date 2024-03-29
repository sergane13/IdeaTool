# Generated by Django 2.1.15 on 2021-01-15 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('optimism_1', models.CharField(blank=True, max_length=75, null=True)),
                ('optimism_1_grade', models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, null=True)),
                ('optimism_2', models.TextField(blank=True, null=True)),
                ('optimism_3', models.TextField(blank=True, null=True)),
                ('neutralism_1', models.TextField(blank=True, null=True)),
                ('neutralism_1_grade', models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, null=True)),
                ('neutralism_2', models.TextField(blank=True, null=True)),
                ('neutralism_2_number', models.IntegerField(blank=True, default=0, null=True)),
                ('neutralism_2_moments', models.TextField(blank=True, null=True)),
                ('neutralism_2_times', models.IntegerField(blank=True, default=0, null=True)),
                ('neutralism_2_grade', models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, null=True)),
                ('neutralism_3', models.TextField(blank=True, null=True)),
                ('neutralism_3_grade', models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, null=True)),
                ('neutralism_4_team', models.TextField(blank=True, null=True)),
                ('pessimism_1', models.TextField(blank=True, null=True)),
                ('pessimism_1_grade', models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='0', max_length=2, null=True)),
                ('pessimism_2', models.TextField(blank=True, null=True)),
                ('pessimism_2_grade', models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=0, max_length=2, null=True)),
            ],
        ),
    ]
