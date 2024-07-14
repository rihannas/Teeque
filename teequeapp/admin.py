from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Rating)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(CustomUser)



