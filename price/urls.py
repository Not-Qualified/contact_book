from django.urls import path
from .views import CreatePriceView, ListPriceView

urlpatterns = [
	path("create/", CreatePriceView.as_view(), name="price-create"),
	path("list/", ListPriceView.as_view(), name="price-list"),
]