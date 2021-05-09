# Generated by Django 3.2 on 2021-05-09 09:27

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', myapp.models.AccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('sector', models.CharField(max_length=16)),
                ('brand_name', models.CharField(max_length=40)),
                ('mutual', models.CharField(max_length=40)),
                ('franchise_start_date', models.CharField(max_length=40)),
                ('franchise_months', models.IntegerField()),
                ('num_of_franchise', models.IntegerField()),
                ('num_of_employees', models.IntegerField()),
                ('num_of_open', models.IntegerField()),
                ('num_of_quit', models.IntegerField()),
                ('num_of_cancel', models.IntegerField()),
                ('num_of_name_changing', models.IntegerField()),
                ('average_sales', models.IntegerField()),
                ('average_sales_per_area', models.IntegerField()),
                ('franchise_fee', models.IntegerField()),
                ('education_fee', models.IntegerField()),
                ('deposit', models.IntegerField()),
                ('other_cost', models.IntegerField()),
                ('startup_cost', models.IntegerField()),
                ('cost_per_area', models.IntegerField()),
                ('standard_area', models.IntegerField()),
                ('total_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Headquarter',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('mutual', models.CharField(max_length=40)),
                ('representative', models.CharField(max_length=40)),
                ('register_law_date', models.CharField(max_length=40)),
                ('register_biz_date', models.CharField(max_length=40)),
                ('representative_number', models.CharField(max_length=40)),
                ('fax_number', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=128)),
                ('biz_type', models.CharField(max_length=40)),
                ('law_number', models.CharField(max_length=40)),
                ('biz_number', models.CharField(max_length=40)),
                ('assets_2020', models.FloatField()),
                ('liabilities_2020', models.FloatField()),
                ('equity_2020', models.FloatField()),
                ('sales_2020', models.FloatField()),
                ('income_2020', models.FloatField()),
                ('net_income_2020', models.FloatField()),
                ('assets_2019', models.FloatField()),
                ('liabilities_2019', models.FloatField()),
                ('equity_2019', models.FloatField()),
                ('sales_2019', models.FloatField()),
                ('income_2019', models.FloatField()),
                ('net_income_2019', models.FloatField()),
                ('assets_2018', models.FloatField()),
                ('liabilities_2018', models.FloatField()),
                ('equity_2018', models.FloatField()),
                ('sales_2018', models.FloatField()),
                ('income_2018', models.FloatField()),
                ('net_income_2018', models.FloatField()),
                ('assets_2017', models.FloatField()),
                ('liabilities_2017', models.FloatField()),
                ('equity_2017', models.FloatField()),
                ('sales_2017', models.FloatField()),
                ('income_2017', models.FloatField()),
                ('net_income_2017', models.FloatField()),
                ('opening_2020', models.IntegerField()),
                ('closing_2020', models.IntegerField()),
                ('name_change_2020', models.IntegerField()),
                ('opening_2019', models.IntegerField()),
                ('closing_2019', models.IntegerField()),
                ('name_change_2019', models.IntegerField()),
                ('opening_2018', models.IntegerField()),
                ('closing_2018', models.IntegerField()),
                ('name_change_2018', models.IntegerField()),
                ('opening_2017', models.IntegerField()),
                ('closing_2017', models.IntegerField()),
                ('name_change_2017', models.IntegerField()),
                ('num_of_correction', models.IntegerField()),
                ('num_loss_of_law', models.IntegerField()),
                ('num_of_sentences', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('do', models.CharField(max_length=16)),
                ('sigu', models.CharField(max_length=32)),
                ('dong', models.CharField(max_length=16)),
                ('population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StoreAddress',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('sector', models.CharField(max_length=16)),
                ('brand_name', models.CharField(max_length=40)),
                ('do', models.CharField(max_length=16)),
                ('sigu', models.CharField(max_length=32)),
                ('dong', models.CharField(max_length=16)),
                ('longitude', models.CharField(max_length=16)),
                ('latitude', models.CharField(max_length=16)),
            ],
        ),
    ]
