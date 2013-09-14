######################################
haystack + django + elasticsearch メモ
######################################

::

    $ curl https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.3.tar.gz
    $ tar xvfz elasticsearch-0.90.3.tar.gz
    $ cd elasticsearch-0.90.3
    $ /bin/elasticsearch -f

    $ python manage.py syncdb --noinput

    $ python manage.py shell

    $ python manage.py shell
    >>> from shop.models import Product
    >>> Product(name='a', price=1000).save()
    >>> Product(name='b', price=10000).save()
    >>> Product(name='c', price=100000).save()
    >>> Product(name='d', price=100000, category1=1).save()

::

    CATEGORY1 = (
        (0, 'Aaa'),
        (1, 'Bbb'),
    )

    CATEGORY2 = (
        (0, 'Ccc'),
        (1, 'Ddd'),
    )

    CATEGORY3 = (
        (0, 'Eee'),
        (1, 'Fff'),
    )

::

    def update_price_range(sender, instance, **kwargs):
        price = instance.price
        if 0 <= price <= 5000:
            instance.price_range = 0
        elif 5000 < price <= 10000:
            instance.price_range = 1
        elif 10000 < price <= 20000:
            instance.price_range = 2
        elif 20000 < price <= 30000:
            instance.price_range = 3
        elif 30000 < price <= 50000:
            instance.price_range = 4
        else:
            instance.price_range = 5
    pre_save.connect(update_price_range, sender=Product)

::

    >>> from haystack.query import SearchQuerySet
    >>> SearchQuerySet().facet('price_range').models(Product).facet_counts()
    {u'dates': {},
     u'fields': {'price_range': [(5, 2), (1, 1), (0, 1)]},
     u'queries': {}}
    >>> SearchQuerySet().facet('category1').models(Product).facet_counts()
    {u'dates': {},
     u'fields': {'category1': [(u'0', 3), (u'1', 1)]},
     u'queries': {}}

