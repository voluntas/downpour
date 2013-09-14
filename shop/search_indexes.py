import datetime

from haystack import indexes
from .models import Product

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    price = indexes.IntegerField(model_attr='price')

    price_range = indexes.IntegerField(model_attr='price_range', faceted=True)

    category1 = indexes.CharField(model_attr='category1', faceted=True)
    category2 = indexes.CharField(model_attr='category2', faceted=True)
    category3 = indexes.CharField(model_attr='category3', faceted=True)

    check1 = indexes.BooleanField(model_attr='check1', faceted=True)
    check2 = indexes.BooleanField(model_attr='check2', faceted=True)
    check3 = indexes.BooleanField(model_attr='check3', faceted=True)

    created_at = indexes.DateTimeField(model_attr='created_at')
    updated_at = indexes.DateTimeField(model_attr='updated_at')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(updated_at__lte=datetime.datetime.now())
