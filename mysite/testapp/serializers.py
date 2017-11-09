from rest_framework import serializers
from testapp.models import Shopping, ShoppingItem, ShopingItemBase


class CustomSerializer(serializers.BaseSerializer):
     def to_representation(self, obj):
        result = dict()
        fields = obj.get_model_fields()
        for field in fields:
            field_as_str = str(field).split('.')[-1]
            value = str(getattr(obj, field_as_str))
            result[field_as_str] = value
        return result

class ShopingItemBaseSerializer(serializers.ModelSerializer):
	item_type = CustomSerializer(source='child')
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
# item_type = ShopingItemBaseSerializer(source='child')