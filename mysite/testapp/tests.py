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

stream = BytesIO(b'{"rix": 12, "ritype": "normal1", "data": {"name": "skuska", "color": "black"}}')
#stream = BytesIO(b'{"name": "test", "issued": "2017-11-11T22:46:50.279797Z", "printed": false, "rtype": "normal", "items": [{"rix": 12, "ritype": "normal1", "data": {"name": "skuska", "color": "black"}}, {"rix": 13, "ritype": "normal2", "data": {"title": "title", "text": "text"}}]}')
data = JSONParser().parse(stream)
print(data)

from testapp.serializers import ShoppingSerializer, ShoppingItemSerializer
from testapp.models import Shopping, ShoppingItem, ShoppingItemNormal1, ShoppingItemNormal2
data = {
	'shopping' : s.id,
	'rix'      : 12,
	'ritype'   : "normal1",
	'child'     : {"nams": "skuska", "color": "black"},
	'username' : 'Dart'
}
serializer = ShoppingItemSerializer(data=data)
print(serializer.is_valid())

print(serializer.validated_data)
print(serializer.errors)

serializer.save()