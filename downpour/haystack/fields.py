from haystack.fields import CharField as BaseCharField

class AnalyzerFieldMixin(object):

    def __init__(self, **kwargs):
        self.analyzer = kwargs.pop('analyzer', None)
        super(AnalyzerFieldMixin, self).__init__(**kwargs)

class CharField(AnalyzerFieldMixin, BaseCharField):
    pass
