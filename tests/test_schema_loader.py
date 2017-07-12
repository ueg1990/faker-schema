import contextlib
import json
import os
import tempfile
import unittest

from faker_schema.schema_loader import load_json_from_file, load_json_from_string


class TestFakerSchema(unittest.TestCase):

	def test_load_json_from_string(self):
		schema_json_string = '{"Full Name": "name", "Address": "address", "Email": "email"}'
		schema = load_json_from_string(schema_json_string)

		self.assertEqual(schema, {'Full Name': 'name', 'Address': 'address', 'Email': 'email'})

	def test_load_json_from_string_incorrect_json(self):
		schema_json_string = '{"Full Name": "name", }'
		with self.assertRaises(ValueError):
			load_json_from_string(schema_json_string)

	@contextlib.contextmanager
	def _write_to_temp_file(self, data, write_to_json=False):
		with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
			if write_to_json:
				json.dump(data, temp_file)
			else:
				temp_file.write(data)
		try:
			yield temp_file.name
		finally:
			os.remove(temp_file.name)
	
	def test_load_json_from_file(self):
		schema = {'Full Name': 'name', 'Address': 'address', 'Email': 'email'}
		with self._write_to_temp_file(schema, write_to_json=True) as temp_file:
			schema = load_json_from_file(temp_file)
			self.assertEqual(schema, {'Full Name': 'name', 'Address': 'address', 'Email': 'email'})

	def test_load_json_from_file_incorrect_json(self):
		schema = '{"Full Name": ["name", "place", ]}'
		with self._write_to_temp_file(schema) as temp_file:
			with self.assertRaises(ValueError):
				load_json_from_file(temp_file)