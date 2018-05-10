__all__ = ['Caller']


class Caller(object):

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def __call__(self, faker):
        return getattr(faker, self.name)(*self.args, **self.kwargs)
