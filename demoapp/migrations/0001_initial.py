# Generated by Django 4.1.3 on 2022-11-09 09:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyMaster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('fincode', models.IntegerField(blank=True, null=True)),
                ('scripcode', models.IntegerField(blank=True, null=True)),
                ('scrip_name', models.CharField(blank=True, max_length=100, null=True)),
                ('scrip_group', models.CharField(blank=True, max_length=3, null=True)),
                ('compname', models.CharField(blank=True, max_length=100, null=True)),
                ('ind_code', models.IntegerField(blank=True, null=True)),
                ('hse_code', models.IntegerField(blank=True, null=True)),
                ('symbol', models.CharField(blank=True, max_length=100, null=True)),
                ('series', models.CharField(blank=True, max_length=5, null=True)),
                ('isin', models.CharField(blank=True, max_length=15, null=True)),
                ('s_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rformat', models.CharField(blank=True, max_length=5, null=True)),
                ('fformat', models.CharField(blank=True, max_length=5, null=True)),
                ('chairman', models.CharField(blank=True, max_length=100, null=True)),
                ('mdir', models.CharField(blank=True, max_length=100, null=True)),
                ('cosec', models.CharField(blank=True, max_length=100, null=True)),
                ('inc_month', models.CharField(blank=True, max_length=10, null=True)),
                ('inc_year', models.IntegerField(blank=True, null=True)),
                ('fv', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('sublisting', models.CharField(blank=True, max_length=50, null=True)),
                ('flag', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stockexchangemaster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('stk_id', models.IntegerField(blank=True, null=True)),
                ('stk_name', models.CharField(blank=True, max_length=100, null=True)),
                ('flag', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complistings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('fincode', models.IntegerField(blank=True, null=True)),
                ('stk_id', models.IntegerField(blank=True, null=True)),
                ('flag', models.CharField(blank=True, max_length=1, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demoapp.companymaster')),
                ('stock_exchange', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demoapp.stockexchangemaster')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyEquity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('fincode', models.IntegerField(blank=True, null=True)),
                ('year_end', models.IntegerField(blank=True, null=True)),
                ('no_shs_subscribed', models.IntegerField(blank=True, null=True)),
                ('latest_equity', models.FloatField(blank=True, null=True)),
                ('latest_reserve', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('mcap', models.FloatField(blank=True, null=True)),
                ('company_yield', models.FloatField(blank=True, null=True)),
                ('fv', models.IntegerField(blank=True, null=True)),
                ('booknavpershare', models.FloatField(blank=True, null=True)),
                ('ttm_yearend', models.IntegerField(blank=True, null=True)),
                ('ttmeps', models.FloatField(blank=True, null=True)),
                ('ttmpe', models.FloatField(blank=True, null=True)),
                ('price_sales', models.FloatField(blank=True, null=True)),
                ('ev_sales', models.FloatField(blank=True, null=True)),
                ('mcap_sales', models.FloatField(blank=True, null=True)),
                ('ev', models.FloatField(blank=True, null=True)),
                ('price_bv', models.FloatField(blank=True, null=True)),
                ('ev_ebitda', models.FloatField(blank=True, null=True)),
                ('ttmceps', models.FloatField(blank=True, null=True)),
                ('price_ceps', models.FloatField(blank=True, null=True)),
                ('pricedate', models.CharField(blank=True, max_length=100, null=True)),
                ('stk_exchange', models.CharField(blank=True, max_length=5, null=True)),
                ('flag', models.CharField(blank=True, max_length=1, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demoapp.companymaster')),
                ('stock_exchange', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demoapp.stockexchangemaster')),
            ],
        ),
    ]
