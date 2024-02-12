# Generated by Django 4.1.4 on 2023-02-18 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0003_temp_detail_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
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
            ],
        ),
        migrations.CreateModel(
            name='Temp_data',
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
                ('availabe', models.BooleanField(default=True)),
                ('otp', models.CharField(max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Temp_detail',
        ),
    ]
