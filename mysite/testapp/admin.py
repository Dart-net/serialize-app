from django.contrib import admin

# Register your models here.
from .models import Shopping, ShoppingItem, ShoppingItemNormal, ShoppingItemNormal2

admin.site.register(Shopping)
admin.site.register(ShoppingItemNormal)
admin.site.register(ShoppingItemNormal2)
admin.site.register(ShoppingItem)


