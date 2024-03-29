# Generated by Django 4.1.5 on 2023-02-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0005_donor_detail_delete_candidates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor_detail',
            name='age',
            field=models.IntegerField(help_text='Age must be greater then 18. and less then 45'),
        ),
        migrations.AlterField(
            model_name='donor_detail',
            name='mobile',
            field=models.CharField(max_length=23),
        ),
    ]
