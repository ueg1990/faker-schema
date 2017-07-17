faker-schema
============

Generate fake data using `joke2k's
faker <https://github.com/joke2k/faker>`__ and your own schema.

Installation
------------

.. code:: bash

    pip install faker-schema

Usage
-----

Getting started
^^^^^^^^^^^^^^^

.. code:: python


    from faker_schema.faker_schema import FakerSchema

    schema = {'employee_id': 'uuid4', 'employee_name': 'name', 'employee address': 'address',
              'email_address': 'email'}
    faker = FakerSchema()
    data = faker.generate_fake(schema)
    print(data)
    # {'employee_id': '956f0cf3-a954-5bff-0aaf-ee0e1b7e1e1b', 'employee_name': 'Adam Wells',
    #  'employee address': '189 Kyle Springs Suite 110\nNorth Robin, OR 73512',
    #  'email_address': 'jmcgee@gmail.com'}


This library is dependent on `faker <https://github.com/joke2k/faker>`__
for available schema types. Faker provides a wide variety of data types
via providers. For a list of available providers, checkout
`Providers <http://faker.readthedocs.io/en/master/providers.html>`__ and
`Community
Providers <http://faker.readthedocs.io/en/master/communityproviders.html>`__

Once you know what types you want to generate your fake data, you can
start defining your own schema

Defining your schema
^^^^^^^^^^^^^^^^^^^^

The expected schema is a dictionary, where the keys are field names and
the values are the types of the fields. The schema dictionay can have
nested dictionaries and lists too.

Loading schemas
^^^^^^^^^^^^^^^

faker-schema currently provides two ways of loading your schema:

-  JSON file
-  JSON string

.. code:: python

    import json

    from faker_schema.faker_schema import FakerSchema
    from faker_schema.schema_loader import load_json_from_file, load_json_from_string

    schema = load_json_from_file('path_to_json_file')
    faker = FakerSchema()
    data = faker.generate_fake(schema)

    # OR

    json_string = '{"employee_id"": "uuid4", "employee_name": "name"", "employee address":
                    "address", "email_address": "email"}'

    schema = load_json_from_string(json_string)
    faker = FakerSchema()
    data = faker.generate_fake(schema)

You can define your own way of loading a schema, convert it to a Python
dictionary and pass it to the FakerSchema instance. The aim was to
de-couple schema loading/generation from fake data generation. If you
want to contribute more schema loading techniques, please open a GitHub
issue or send a pull request.

Using different locales
^^^^^^^^^^^^^^^^^^^^^^^

The `Faker <https://github.com/joke2k/faker>`__ library provides a list
of different `locales <https://github.com/joke2k/faker#localization>`__.
You can choose your required locale from that list and provide it to the
FakerSchema instance

.. code:: python

    from faker_schema.faker_schema import FakerSchema

    schema = {'employee_id': 'uuid4', 'employee_name': 'name', 'employee address': 'address',
              'email_address': 'email'}
    faker = FakerSchema(locale='it_IT')
    data = faker.generate_fake(schema)
    print(data)
    # {'employee_id': '47f8bb04-fc05-25c9-73cc-e8a22f29ee4e', 'employee_name': 'Caio Negri',
    #  'employee address': 'Stretto Davis 34\nDamico lido, 54802 Vibo Valentia (TR)',
    #  'email_address': 'nunzia19@libero.it'}

More Schema Examples
^^^^^^^^^^^^^^^^^^^^

Nested Dictionary
^^^^^^^^^^^^^^^^^

.. code:: python

    from faker_schema.faker_schema import FakerSchema

    schema = {'EmployeeInfo': {'ID': 'uuid4', 'Name': 'name', 'Contact': {'Email': 'email',
              'Phone Number': 'phone_number'}, 'Location': {'Country Code': 'country_code',
              'City': 'city', 'Country': 'country', 'Postal Code': 'postalcode',
              'Address': 'street_address'}}}
    faker = FakerSchema()
    data = faker.generate_fake(schema)
    # {'EmployeeInfo': {'ID': '0751f889-0d83-d05f-4eeb-16f575c6b4a3', 'Name': 'Stacey Williams',
    #  'Contact': {'Email':'jpatterson@yahoo.com', 'Phone Number': '1-077-859-6393'},
    #  'Location': {'Country Code': 'IE', 'City': 'Dyermouth', 'Country':
    #  'United States Minor Outlying Islands', 'Postal Code': '84239',
    #  'Address': '94806 Joseph Plaza Apt. 783'}}}

Nested List
^^^^^^^^^^^

.. code:: python

    from faker_schema.faker_schema import FakerSchema

    schema = {'Employer': 'name', 'EmployeList': [{'Name': 'name'}, {'Name': 'name'},
              {'Name': 'name'}]}
    faker = FakerSchema()
    data = faker.generate_fake(schema)
    # {'Employer': 'Faith Knapp', 'EmployeList': [{'Name': 'Douglas Bailey'},
    # {'Name': 'Karen Rivera'}, {'Name': 'Linda Vance MD'}]}

Generating a certain number of fake data from given schema
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python


    from faker_schema.faker_schema import FakerSchema

    schema = {'employee_id': 'uuid4', 'employee_name': 'name', 'employee address': 'address',
              'email_address': 'email'}
    faker = FakerSchema()
    data = faker.generate_fake(schema, iterations=4)
    print(data)
    # [{'employee_id': 'e07a7964-9636-bca6-2a58-4a69ac126dc5', 'employee_name':
    # 'Charlene Blankenship', 'employee address': '0431 Edward Mountains Suite 697\nPort Douglas,
    # TX 96239-7277', 'email_address': 'ashley86@yahoo.com'}, {'employee_id':
    # '42b02262-3e0c-cf40-8257-4a0af122dddb', 'employee_name': 'Cheryl Stevens',
    # 'employee address': '48066 Eric Lake\nPhillipshire, MO 57224', 'email_address':
    # 'lisa05@nash.info'}, {'employee_id': '41efbcc4-bb32-9260-b2b3-8fac29782e01',
    # 'employee_name': 'Dennis Campbell', 'employee address':
    # '52418 Diana Mills Suite 590\nEast Mackenzie, HI 16222', 'email_address':
    # 'jennifer39@gmail.com'}, {'employee_id': '80bf12ff-2f3a-6db6-f3a6-14cb50076a46',
    # 'employee_name': 'Jimmy Avery', 'employee address':
    # '6867 Eddie Forest Apt. 735\nBranditon, IL 32717', 'email_address': 'ashley64@griffin.com'}]

BYOP (Bring Your Own Provider)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are using a community provider or you created your own provider,
you can use those with faker-schema as well. I will use the provider,
`faker\_web <https://github.com/thiagofigueiro/faker_web>`__ as an
example.

After `installing <https://github.com/thiagofigueiro/faker_web#usage>`__
faker\_web,

.. code:: python

    from faker import Faker
    from faker_schema import FakerSchema
    from faker_web import WebProvider

    fake = Faker()
    fake.add_provider(WebProvider)

    faker = FakerSchema(faker=fake)
    headers_schema = {'Content-Type': 'content_type', 'Server': 'server_token'}
    fake_headers = faker.generate_fake(headers_schema)
    print(fake_headers)
    # {'Content-Type': 'application/json', 'Server': 'Apache/2.0.51 (Ubuntu)'} 

Development
-----------

Running tests
^^^^^^^^^^^^^

-  Using make

.. code:: bash

    make test

-  Using nose

.. code:: bash

    nosetests 

-  Using nose with coverage

.. code:: bash

    nosetests --with-coverage --cover-package=faker_schema --cover-erase -v --cover-html

Running flake8
^^^^^^^^^^^^^^

-  Using make

.. code:: bash

    make flake8

-  Using flake8

.. code:: bash

    flake8 --max-line-length 99 faker_schema/ tests/

Author
------

Usman Ehtesham Gul (`ueg1990 <https://github.com/ueg1990>`__) -
uehtesham90@gmail.com

Contribute
----------

If you want to add any new features, or improve existing one or if you
find bugs, please open a GitHub issue or feel free to send a pull
request. If you have any questions or need help/mentoring with
contributions, feel free to contact me via email
