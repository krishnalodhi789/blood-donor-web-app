# Generated by Django 4.1.4 on 2023-02-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0004_candidates_temp_data_delete_temp_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=32)),
                ('age', models.IntegerField(help_text='Age must be greater then 18.')),
                ('state', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('area', models.CharField(max_length=32)),
                ('available', models.BooleanField(default=True)),
                ('blood_group', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Candidates',
        ),
    ]
