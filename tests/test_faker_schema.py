import unittest
import datetime
from faker_schema.faker_schema import FakerSchema


class MockFaker(object):

    def name(self):
        return 'John Doe'

    def address(self):
        return '4570 Jaime Plains Suite 188\nNew Johnny, DE 89711-3908'

    def email(self):
        return 'towen@nelson.biz'

    def street_address(self):
        return '869 Massey Tunnel'

    def city(self):
        return 'Copenhagen'

    def country(self):
        return 'Denmark'

    def postalcode(self):
        return '17204'

    def date_of_birth(self):
        return datetime.date(1963, 4, 9)

    def random_int(self, min=0, max=100):
        return 63


class TestFakerSchema(unittest.TestCase):

    def setUp(self):
        self.faker_schema = FakerSchema(faker=MockFaker())

    def test_generate_fake_flat_schema(self):
        schema = {'Full Name': 'name', 'Address': 'address', 'Email': 'email'}
        data = self.faker_schema.generate_fake(schema)

        self.assertIsInstance(data, dict)

    def test_generate_fake_flat_schema_4_iterations(self):
        schema = {'Full Name': 'name', 'Address': 'address', 'Email': 'email'}
        data = self.faker_schema.generate_fake(schema, iterations=4)

        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 4)

    def test_generate_fake_nested_schema(self):
        schema = {'Full Name': 'name', 'Location': {'Address': 'street_address', 'City': 'city',
                  'Country': 'country', 'Postal Code': 'postalcode'}}
        data = self.faker_schema.generate_fake(schema)

        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['Location'], dict)

    def test_generate_fake_schema_with_list(self):
        schema = {'Employer': 'name', 'EmployeeList': [{'Employee1': 'name'},
                  {'Employee2': 'name'}]}
        data = self.faker_schema.generate_fake(schema)

        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['EmployeeList'], list)

    def test_generate_fake_schema_with_choices(self):
        schema = {
            'Person': 'name',
            'Gender': '(Male,Female)'  # simliar to fuzzy choices
        }
        data = self.faker_schema.generate_fake(schema)

        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['Gender'], str)

    def test_generate_fake_schema_with_date(self):
        schema = {
            'Person': 'name',
            'Gender': '(Male,Female)',
            'BirthDay': 'date_of_birth'  # returns date with isoformat
        }
        data = self.faker_schema.generate_fake(schema)

        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['BirthDay'], str)

    def test_generate_fake_schema_with_fake_args(self):
        schema = {
            'Person': 'name',
            'Gender': '(Male,Female)',
            'BirthDay': 'date_of_birth',
            'Age': 'random_int(18,80)'  # passing arguments (age betweeen 18 and 80)
        }
        data = self.faker_schema.generate_fake(schema)

        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['Age'], int)

    def test_generate_fake_schema_with_fake_kargs(self):
        schema = {
            'Person': 'name',
            'Gender': '(Male,Female)',
            'BirthDay': 'date_of_birth',
            'Age': 'random_int(min=18,max=80)'  # passing named arguments (age betweeen min=18 and max=80)
        }
        data = self.faker_schema.generate_fake(schema)

        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['Age'], int)
