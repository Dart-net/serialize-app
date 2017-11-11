from django.test import TestCase
from testapp.serializers import ShoppingSerializer, ShoppingItemSerializer
from testapp.models import Shopping, ShoppingItem, ShoppingItemNormal1, ShoppingItemNormal2
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from django.utils.six import BytesIO

s = Shopping(name='test')
s.save()

si = ShoppingItem(shopping=s,rix=12)
si.save()
sin = ShoppingItemNormal1(name='skuska', color='black', shopping_item=si)
sin.save()

si = ShoppingItem(shopping=s,rix=13)
si.save()
sin = ShoppingItemNormal2(title='title', text='text', shopping_item=si)
sin.save()

sis = ShoppingItemSerializer(si)
ss = ShoppingSerializer(s)
#print(sis.data)
#print(ss.data)
#print(JSONRenderer().render(ss.data))
print(json.dumps(ss.data))
