from django.core.management.base import BaseCommand, CommandError
from testapp.serializers import ShoppingSerializer, ShoppingItemSerializer
from testapp.models import Shopping, ShoppingItem, ShoppingItemNormal1, ShoppingItemNormal2

class Command(BaseCommand):
    help = 'Test for serializers'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Create test item dict for deserializing
        shopping = Shopping.objects.create(name='Test shopping')
        print('Create test shopping %s' % shopping.id)
        data = {
            'shopping' : shopping.id, # id of Shopping
            'rix'      : 12,
            'ritype'   : "normal1",
            'child'     : {"name": "Fabien", "color": "black"},
            # 'child'     : {"title": "Dart", "text": "white"},
        }
        print('Create from data %s' % data)
        serializer = ShoppingItemSerializer(data=data) # create serializer with test data
        if serializer.is_valid():
            item = serializer.save() # save serialize(create new item)
            print('Item: %s' % str(item))
            print('Child %s' % str(item.details))
            s_item = ShoppingItemSerializer(item) # Now try to serializer test item object
            print('Serialize item %s' % s_item.data)
        else:
            print('Errors: ', serializer.errors)

