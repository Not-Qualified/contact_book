from django.contrib import admin
from .models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
	list_display = ["customer", "mobile_one", "city", "country", "date_added", ]

	def customer(self, obj):
		return f"{obj.first_name} {obj.last_name}"

	customer.short_description = "Name"


admin.site.register(Customer, CustomerAdmin)