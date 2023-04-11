# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['adaptable',
 'adaptable._data_access',
 'adaptable._data_access.deletion',
 'adaptable._data_access.query',
 'adaptable._data_access.update',
 'adaptable.cleaning',
 'adaptable.refactoring']

package_data = \
{'': ['*']}

install_requires = \
['black>=23.3.0,<24.0.0',
 'boto3>=1.26.103,<2.0.0',
 'pandas>=1.5.3,<2.0.0',
 'psycopg2>=2.9.5,<3.0.0']

setup_kwargs = {
    'name': 'adaptable',
    'version': '0.1.5',
    'description': '',
    'long_description': None,
    'author': 'Paul Couturier',
    'author_email': 'paul.couturier@ovrsea.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
