import json 
import sys
import os
import django

sys.path.append('C:\SageOne\SageoneDemo\SageoneDemo')
os.environ['DJANGO_SETTINGS_MODULE'] = 'SageoneDemo.settings'
django.setup()

from demoapp.models import CompanyMaster,CompanyEquity,Complistings,Stockexchangemaster

files = [
            # "C:\SageOne\SageoneDemo\demoapp\datafiles\Companymaster.txt",
            # "C:\SageOne\SageoneDemo\demoapp\datafiles\company_equity.txt",
            # "C:\SageOne\SageoneDemo\demoapp\datafiles\Complistings.txt",
            # "C:\SageOne\SageoneDemo\demoapp\datafiles\Stockexchangemaster.txt"
]

if __name__=="__main__":
    for file in files:
        filename = (file.split(".")[0]).split('\\')[-1]

        if filename == "Companymaster":
            with open(file) as f:
                d = json.load(f)
                newdict = {}
                for item in d['Table']:
                    for key,value in item.items():
                        if key.lower()=="fincode" or key.lower()=="scripcode" or key.lower()=="ind_code" or key.lower()=="hse_code" or key.lower()=="inc_year" or key.lower()=="fv":
                            print(value)
                            if value:
                                value = int(value)
                            else:
                                print("--->") 
                                value=0
                        newdict[key.lower()]=value
                    CompanyMaster.objects.create(**newdict)

        elif filename == "company_equity":
            with open(file) as f:
                d = json.load(f)
                newdict = {}
                for item in d['Table']:
                    for key,value in item.items():
                        if key == "YIELD":  
                            key = "company_yield"
                        print(key)
                        if key.lower()=="fincode" or key.lower()=="year_end" or key.lower()=="no_shs_subscribed" or key.lower()=="fv" or key.lower()=="ttm_yearend":
                            print(value)
                            if value:
                                value = int(value)
                            else:
                                print("--->") 
                                value=0

                        #latest_equity,latest_reserve,price,mcap,company_yield,booknavpershare,ttmeps,ttmpe,price_sales,ev_sales,mcap_sales,ev,price_bv,ev_ebitda,ttmceps,price_ceps
                        elif key.lower() == "latest_equity" or key.lower() == "latest_reserve" or key.lower() == "price" or key.lower() == "mcap" or key.lower() == "company_yield" or key.lower() == "booknavpershare" or key.lower() == "ttmeps" or key.lower() == "ttmpe" or key.lower() == "price_sales" or key.lower() == "ev_sales" or key.lower() == "mcap_sales" or key.lower() == "ev" or key.lower() == "price_bv" or key.lower() == "ev_ebitda" or key.lower() == "ttmceps" or key.lower() == "price_ceps" :
                            print(value)
                            if value:
                                value = float(value)
                            else:
                                print("--->") 
                                value=0.0
                        newdict[key.lower()]=value
                    CompanyEquity.objects.create(**newdict)
                    
                    
        elif filename == "Complistings":
            with open(file) as f:
                d = json.load(f)
                newdict = {}
                for item in d['Table']:
                    for key,value in item.items():
                        if key.lower()=="fincode" or key.lower()=="stk_id":
                            print(value)
                            if value:
                                value = int(value)
                            else:
                                print("--->") 
                                value=0
                        newdict[key.lower()]=value
                    Complistings.objects.create(**newdict)

        elif filename == "Stockexchangemaster":
            with open(file) as f:
                d = json.load(f)
                newdict = {}
                for item in d['Table']:
                    for key,value in item.items():
                        if key.lower()=="stk_id":
                            print(value)
                            if value:
                                value = int(value)
                            else:
                                print("--->") 
                                value=0
                        newdict[key.lower()]=value
                    Stockexchangemaster.objects.create(**newdict)