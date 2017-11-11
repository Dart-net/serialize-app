from django.contrib import admin

# Register your models here.
from .models import Shopping, ShoppingItem, ShoppingItemNormal1, ShoppingItemNormal2

admin.site.register(Shopping)
admin.site.register(ShoppingItemNormal1)
admin.site.register(ShoppingItemNormal2)
admin.site.register(ShoppingItem)


