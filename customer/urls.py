"""laxmi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (CreateCustomerView, ListCustomerView, DetailCustomerView, 
					UpdateCustomerView, DeleteCustomerView, )

urlpatterns = [
    path("", CreateCustomerView.as_view(), name="customer-create"),
    path("list/", ListCustomerView.as_view(), name="customer-list"),
    path("detail/<int:pk>/", DetailCustomerView.as_view(), name="customer-detail"),
    path("update/<int:pk>/", UpdateCustomerView.as_view(), name="customer-update"),
    path("delete/<int:pk>/", DeleteCustomerView.as_view(), name="customer-delete"),
]
