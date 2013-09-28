import datetime

from haystack import indexes
from celery_haystack.indexes import CelerySearchIndex

from downpour.haystack.fields import CharField
from .models import Product

class ProductIndex(CelerySearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    name = CharField(model_attr='name', analyzer='kuromoji_analyzer')
    price = indexes.IntegerField(model_attr='price')

    price_range = indexes.IntegerField(model_attr='price_range', faceted=True)

    category1 = indexes.CharField(model_attr='category1', faceted=False, stored=False)
    category2 = indexes.CharField(model_attr='category2', faceted=True, stored=True)
    category3 = indexes.CharField(model_attr='category3', stored=False, faceted=True)

    # check1 = indexes.BooleanField(model_attr='check1', stored=False, faceted=True)
    # check2 = indexes.BooleanField(model_attr='check2', stored=False, faceted=True)
    # check3 = indexes.BooleanField(model_attr='check3', stored=False, faceted=True)

    created_at = indexes.DateTimeField(model_attr='created_at')
    updated_at = indexes.DateTimeField(model_attr='updated_at')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(updated_at__lte=datetime.datetime.now())
