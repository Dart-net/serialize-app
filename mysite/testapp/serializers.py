from rest_framework import serializers
from testapp.models import Shopping, ShoppingItem, ShopingItemBase

class ShopingItemBaseSerializer(serializers.ModelSerializer):
	# item_type = serializers.ReadOnlyField(source='child')
	item_type = ShopingItemBaseSerializer(source='child')
	class Meta:
		model = ShopingItemBase
		fields = '__all__'

class ShoppingItemSerializer(serializers.ModelSerializer):
    base_item = ShopingItemBaseSerializer(source='details')
    class Meta:
        model = ShoppingItem
        fields = '__all__'

class ShoppingSerializer(serializers.ModelSerializer):
    items = ShoppingItemSerializer(source='shoppingitem_set', many=True)
    class Meta:
        model = Shopping
        fields = '__all__'


'''
from testapp.serializers import ShoppingSerializer, ShoppingItemSerializer
from testapp.models import Shopping, ShoppingItem
sh = Shopping.objects.get(id=2)
s = ShoppingSerializer(sh)
'''