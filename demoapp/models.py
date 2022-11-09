from django.db import models
import uuid 


class CompanyMaster(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    fincode = models.IntegerField(blank=True, null=True)
    scripcode = models.IntegerField(blank=True, null=True)
    scrip_name = models.CharField(max_length=100, blank=True, null=True)
    scrip_group = models.CharField(max_length=3, blank=True, null=True)
    compname = models.CharField(max_length=100, blank=True, null=True)
    ind_code = models.IntegerField(blank=True, null=True)
    hse_code = models.IntegerField(blank=True, null=True)
    symbol = models.CharField(max_length=100, blank=True, null=True)
    series = models.CharField(max_length=5, blank=True, null=True)
    isin = models.CharField(max_length=15, blank=True, null=True)
    s_name = models.CharField(max_length=100, blank=True, null=True)
    rformat = models.CharField(max_length=5, blank=True, null=True)
    fformat = models.CharField(max_length=5, blank=True, null=True)
    chairman = models.CharField(max_length=100, blank=True, null=True)
    mdir = models.CharField(max_length=100, blank=True, null=True)
    cosec = models.CharField(max_length=100, blank=True, null=True)
    inc_month = models.CharField(max_length=10, blank=True, null=True)
    inc_year = models.IntegerField(blank=True, null=True)
    fv = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50,blank=True, null=True)
    sublisting = models.CharField(max_length=50, blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)



class Stockexchangemaster(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)    
    stk_id = models.IntegerField(blank=True, null=True)
    stk_name = models.CharField(max_length=100, blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)


class Complistings(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)    
    fincode = models.IntegerField(blank=True, null=True)
    stk_id = models.IntegerField(blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)
    company = models.ForeignKey(CompanyMaster,on_delete=models.CASCADE, blank=True, null=True)
    stock_exchange = models.ForeignKey(Stockexchangemaster,on_delete = models.CASCADE, blank=True, null=True)

class CompanyEquity(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)    
    fincode = models.IntegerField(blank=True, null=True)    
    year_end = models.IntegerField(blank=True, null=True)
    no_shs_subscribed = models.IntegerField(blank=True, null=True)
    latest_equity = models.FloatField(blank=True, null=True)
    latest_reserve = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    mcap = models.FloatField(blank=True, null=True)
    company_yield = models.FloatField(blank=True, null=True)
    fv = models.IntegerField(blank=True, null=True)
    booknavpershare = models.FloatField(blank=True, null=True)
    ttm_yearend = models.IntegerField(blank=True, null=True)
    ttmeps = models.FloatField(blank=True, null=True)
    ttmpe = models.FloatField(blank=True, null=True)
    price_sales = models.FloatField(blank=True, null=True)
    ev_sales = models.FloatField(blank=True, null=True)
    mcap_sales = models.FloatField(blank=True, null=True)
    ev = models.FloatField(blank=True, null=True)
    price_bv = models.FloatField(blank=True, null=True)
    ev_ebitda = models.FloatField(blank=True, null=True)
    ttmceps = models.FloatField(blank=True, null=True)
    price_ceps = models.FloatField(blank=True, null=True)
    pricedate = models.CharField(max_length=100, blank=True, null=True)
    stk_exchange = models.CharField(max_length=5, blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)
    company = models.ForeignKey(CompanyMaster,on_delete=models.CASCADE, blank=True, null=True)
    stock_exchange = models.ForeignKey(Stockexchangemaster,on_delete = models.CASCADE, blank=True, null=True)