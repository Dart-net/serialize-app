from django.db import models

# Create your models here.
#import datetime
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Shopping(models.Model):
    """ The class represents Shopping basic info """

    RECEIPT_TYPE = (
        ('type1', 'Basic'),
        ('type2', 'Intermediate'),
        ('type3', 'Advanced'),
    )

    name = models.CharField(max_length=128, blank=False)
    issued = models.DateTimeField(auto_now_add=True)
    printed = models.BooleanField(default=False)
    rtype = models.CharField(max_length=16, choices=RECEIPT_TYPE, default='normal',)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('issued',)


class ShoppingItem(models.Model):

    RECEIPT_ITEM_TYPE = (
        ('normal', 'normal'),
        ('test', 'test')
    )

    shopping = models.ForeignKey('Shopping', on_delete=models.CASCADE,)
    rix = models.PositiveSmallIntegerField()
    ritype = models.CharField(max_length=16, choices=RECEIPT_ITEM_TYPE, default='normal',)

class ShopingItemBase(models.Model):

    SHOPPING_CHILD_CLASS_NAMES = (
        ('shoppingitemnormal', 'shoppingitemnormal'),
        ('shoppingitemnormal2', 'shoppingitemnormal2')
    )

    shopping_item = models.OneToOneField('ShoppingItem', related_name='details', on_delete=models.CASCADE, null=True)
    shopping_type = models.CharField(max_length=255, choices=SHOPPING_CHILD_CLASS_NAMES, default='shoppingitemnormal',)

    @property
    def child(self):
        child = getattr(self, self.shopping_type)
        return child

    def get_model_fields(self):
        return self._meta.fields


class ShoppingItemNormal(ShopingItemBase):
    name = models.CharField(max_length=128, blank=False, default='test')
    color = models.CharField(max_length=128, blank=False, default='blue')

class ShoppingItemNormal2(ShopingItemBase):
    title = models.CharField(max_length=128, blank=False, default='title')
    text = models.CharField(max_length=128, blank=False, default='text')
