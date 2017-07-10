from __future__ import print_function

import json

from faker import Faker
from faker.config import DEFAULT_LOCALE


def load_file(file_path):
    with open(file_path) as f:
        return json.load(f)


class FakerSchema(object):
    
    def __init__(self, schema, faker=None, locale=None, providers=None, includes=None):
        self._faker = faker or Faker(locale=locale, providers=providers, includes=includes)
        self._schema = schema

    @property
    def schema(self):
        return self._schema
        
    def generate_fake(self, iterations=1):
        result = [self._generate_one_fake(self.schema) for _ in range(iterations)]
        return result[0] if len(result) == 1 else result

    def _generate_one_fake(self, schema):
        """
        Recursively traverse schema dictionary and for each "leaf node", evaluate the fake
        value

        Implementation:
        For each key-value pair:
        1) If value is not an iterable (i.e. dict or list), evaluate the fake data (base case)
        2) If value is a dictionary, recurse
        3) If value is a list, iteratively recurse over each item
        """
        data = {}
        for k, v in schema.items():
            if isinstance(v, dict):
                data[k] = self._generate_one_fake(v)
            elif isinstance(v, list):
                data[k] = [self._generate_one_fake(item) for item in v]
            else:
                data[k] = getattr(self._faker, v)()
        return data

    @classmethod
    def from_json_file(cls, json_file, *args, **kwargs):
        try:
            json_data = load_file(json_file)
        except ValueError as e:
            raise ValueError('Given file {} is not a valid JSON file: {}'.format(json_file, e))
        else:    
            return cls(json_data, *args, **kwargs)

    @classmethod
    def from_json_string(cls, json_string, *args, **kwargs):
        try:
            json_data = json.loads(json_string)
        except ValueError as e:
            raise ValueError('Given string is not valid JSON: {}'.format(e))
        else:    
            return cls(json_data, *args, **kwargs)
