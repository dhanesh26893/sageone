from django.contrib import admin
from .models import CompanyMaster,CompanyEquity,Complistings,Stockexchangemaster

admin.site.register(CompanyMaster)
admin.site.register(CompanyEquity)
admin.site.register(Complistings)
admin.site.register(Stockexchangemaster)