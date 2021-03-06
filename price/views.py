from django.shortcuts import render
from django.views.generic import (CreateView, ListView, )
from .models import Price
# Create your views here.

class CreatePriceView(CreateView):
	model = Price
	fields = ["gold_market_price", "gold_bill_price", 
			  "gold_old_ornaments_price", 
			  "gold_24_carat", "gold_22_carat", "gold_18_carat", 
			  "silver_without_bill_price", 
			  "silver_with_bill_price", ]



class ListPriceView(ListView):
	model = Price
	