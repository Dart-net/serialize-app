from django.db import models

# Create your models here.
#import datetime
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Shopping(models.Model):
    """ The class represents Shopping basic info """

    SHOPPING_TYPE = (
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )

    name = models.CharField(max_length=128, blank=False)
    issued = models.DateTimeField(auto_now_add=True)
    printed = models.BooleanField(default=False)
    rtype = models.CharField(max_length=16, choices=SHOPPING_TYPE, default='normal',)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('issued',)

class ShoppingItem(models.Model):

    SHOPPING_ITEM_TYPE = (
        ('normal1', 'Basic'),
        ('normal2', 'Intermediate'),
        ('normal3', 'Advanced'),
    )

    shopping = models.ForeignKey('Shopping', on_delete=models.CASCADE,)
    rix = models.PositiveSmallIntegerField()
    ritype = models.CharField(max_length=16, choices=SHOPPING_ITEM_TYPE, default='normal1',)

class ShoppingItemBase(models.Model):
    shopping_item = models.OneToOneField('ShoppingItem', related_name='details', on_delete=models.CASCADE, null=True)

    @property
    def child(self):
        if self.shopping_item.ritype == 'normal1':
            child = self.shoppingitemnormal1
        elif self.shopping_item.ritype == 'normal2':
            child = self.shoppingitemnormal2
        else:
            child = None
        return child

class ShoppingItemNormal1(ShoppingItemBase):
    name = models.CharField(max_length=128, blank=False, default='meno')
    color = models.CharField(max_length=128, blank=False, default='cierna')

class ShoppingItemNormal2(ShoppingItemBase):
    title = models.CharField(max_length=128, blank=False, default='nazov')
    text = models.CharField(max_length=128, blank=False, default='popis')
