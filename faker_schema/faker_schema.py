from faker import Faker
from .faker_caller import Caller


__all__ = ['FakerSchema']


try:
    string_type = basestring
except NameError:
    string_type = str


class FakerSchema(object):

    def __init__(self, faker=None, locale=None, providers=None, includes=None):
        self._faker = faker or Faker(locale=locale, providers=providers, includes=includes)

    def generate_fake(self, schema, iterations=1):
        result = [self._generate_one_fake(schema) for _ in range(iterations)]
        return result[0] if len(result) == 1 else result

    def _generate_one_fake(self, schema):
        """
        Recursively traverse schema dictionary and for each "leaf node", evaluate the fake
        value

        Implementation:
        For each key-value pair:
        1) If value is not an iterable (i.e. dict or list), evaluate the fake data (base case)
        1) If value is a dictionary, recurse
        2) If value is a list, iteratively recurse over each item
        3) If value is string and faker has method called like value evaluate the fake data
        4) If value is "Caller" object evaluate the fake data
        5) In any other case pass value as is
        """
        data = {}
        for k, v in schema.items():
            if isinstance(v, dict):
                data[k] = self._generate_one_fake(v)
            elif isinstance(v, list):
                data[k] = [self._generate_one_fake(item) for item in v]
            elif isinstance(v, string_type) and hasattr(self._faker, v):
                data[k] = getattr(self._faker, v)()
            elif isinstance(v, Caller):
                data[k] = v(self._faker)
            else:
                data[k] = v
        return data
