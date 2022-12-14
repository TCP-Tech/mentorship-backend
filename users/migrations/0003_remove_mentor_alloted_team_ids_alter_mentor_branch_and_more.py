# Generated by Django 4.1.3 on 2022-12-15 06:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_mentor_codechefid_alter_mentor_codeforcesid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='alloted_team_ids',
        ),
        migrations.AlterField(
            model_name='mentor',
            name='branch',
            field=models.CharField(choices=[('1', 'CSE'), ('2', 'IT'), ('3', 'ECE'), ('4', 'ELEC'), ('5', 'MECH'), ('6', 'CHEM'), ('7', 'CIVIL'), ('8', 'META'), ('9', 'MIN'), ('10', 'BIOMED'), ('11', 'BIOTECH'), ('12', 'MCA')], max_length=8),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='semester',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)]),
        ),
    ]
