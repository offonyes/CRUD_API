from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Category Name'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    # Many-to-Many
    category = models.ManyToManyField('Category', related_name='Product', verbose_name=_('Category'))
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_('Product Name'))
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name=_('Price'))
    stock = models.IntegerField(null=False, blank=False, verbose_name=_('Stock'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
