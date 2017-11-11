from rest_framework import serializers
from testapp.models import Shopping, ShoppingItem, ShoppingItemBase, ShoppingItemNormal1, ShoppingItemNormal2

class ShoppingItemNormal1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItemNormal1
        fields = ('name', 'color')

class ShoppingItemNormal2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItemNormal2
        fields = ('title', 'text')

class CustomSerializer(serializers.Serializer):
    @classmethod
    def _get_serializer(cls, model):
        if model == ShoppingItemNormal1:
            return ShoppingItemNormal1Serializer
        elif model == ShoppingItemNormal2:
            return ShoppingItemNormal2Serializer

    def to_representation(self, instance):
        serializer = self._get_serializer(instance.__class__)
        return serializer(instance, context=self.context).data

#class ShoppingItemBaseSerializer(serializers.ModelSerializer):
#    item_type = CustomSerializer(source='child')
#    class Meta:
#        model = ShoppingItemBase
#        fields = ('item_type',)

class ShoppingItemSerializer(serializers.ModelSerializer):
    data = CustomSerializer(source='details.child')

    class Meta:
        model = ShoppingItem
        fields = ('rix', 'ritype', 'data')

    def to_internal_value(self, data):
        super(ShoppingItemSerializer, self).to_internal_value(data)

#    def validate_data(self, data):
#        pass

    def to_internal_value(self, data):
        super(ShoppingItemSerializer, self).to_internal_value(data)

class ShoppingSerializer(serializers.ModelSerializer):
    items = ShoppingItemSerializer(source='shoppingitem_set', many=True)
    class Meta:
        model = Shopping
        fields = ('name', 'issued', 'printed', 'rtype', 'items')
