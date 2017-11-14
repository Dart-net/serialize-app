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
    def get_serializer(self, model):
        if model == ShoppingItemNormal1:
            return ShoppingItemNormal1Serializer
        elif model == ShoppingItemNormal2:
            return ShoppingItemNormal2Serializer

    def to_representation(self, instance):
        serializer = self.get_serializer(instance.__class__)
        return serializer(instance, context=self.context).data

#class ShoppingItemBaseSerializer(serializers.ModelSerializer):
#    item_type = CustomSerializer(source='child')
#    class Meta:
#        model = ShoppingItemBase
#        fields = ('item_type',)

class ShoppingItemSerializer(serializers.ModelSerializer):
    child = CustomSerializer(source='details.child')

    class Meta:
        model = ShoppingItem
        fields = ('rix', 'ritype', 'shopping', 'child')

    def get_child_class_by_type(self, _type):
        ''' Determine Item child class model by `ritype`. Use elsewhere as static method.'''
        ChildClass = ShoppingItemNormal1Serializer
        if _type == 'normal1':
            ChildClass = ShoppingItemNormal1Serializer
        elif _type == 'normal2':
            ChildClass = ShoppingItemNormal2Serializer
        return ChildClass


    def create(self, validated_data):
        details = validated_data.pop('details')
        child = details['child']
        item = ShoppingItem.objects.create(**validated_data)
        child['shopping_item'] = item
        ChildClass = item.get_child_class() # get child class via instance
        ChildClass.objects.create(**child)
        return item

    def to_internal_value(self, data):
        try:
            ch = data['child']
        except:
            pass
        data  = super(ShoppingItemSerializer, self).to_internal_value(data)
        data['details']['child'] = ch
        return data

    def validate(self, data):
        ch = data['details']['child']
        ChildClass = self.get_child_class_by_type(data['ritype']) # get child via static method
        ChildClass().to_internal_value(ch) #self.child.get_serializer(ChildClass)

        return data

        # _class = self.Meta.model
        # print('Validate:', dir(self))
        # print('Class: ', self.__class__)
        # print('Model: ', )
        # ChildClass = ShoppingItem.
        # print('Current object: ', self)
        # child = data['details']['child']
        # print('Validate child: ', child)

    # def validate_child(self, value):
    #     print('Current object: ', self)

    # def validate_data(self, value):
    #     print('Validate: ', value)
    #     return value


class ShoppingSerializer(serializers.ModelSerializer):
    items = ShoppingItemSerializer(source='shoppingitem_set', many=True)
    class Meta:
        model = Shopping
        fields = ('name', 'issued', 'printed', 'rtype', 'items')
