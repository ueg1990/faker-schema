from faker import Faker
import random
import re


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
                args = []
                kwargs = {}
                if v.startswith("(") and v.endswith(")"):
                    choices = re.findall(r'\w+', v)
                    data[k] = random.choice(choices)  # TODO seed and fake dependency control
                    continue
                elif bool(re.search(r'\w+\(.*\)', v)):
                    tokens = re.findall(r'[\w\=]+', v)
                    v = tokens.pop(0)
                    for token in tokens:
                        if "=" in token:
                            x, y = token.split("=")
                            kwargs[x] = int(y) if y.isdigit() else y
                        else:
                            args.append(int(token) if token.isdigit() else token)
                if v.startswith("date"):
                    data[k] = getattr(self._faker, v)(*args, **kwargs).isoformat()
                else:
                    data[k] = getattr(self._faker, v)(*args, **kwargs)
        return data
