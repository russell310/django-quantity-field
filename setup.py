import io

from os import path
from setuptools import setup, find_packages
from quantity_field import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with io.open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-quantity-field',
    long_description=long_description,
    version='.'.join(str(x) for x in __version__),
    description='Field for Django models that stores multidimensional physical quantities',
    url='https://github.com/catcombo/django-quantity-field',
    author='Evgeniy Krysanov',
    author_email='evgeniy.krysanov@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    keywords='django multiple quantity field',
    packages=find_packages(include=["quantity_field", "quantity_field.*"]),
    install_requires=['pint'],
    include_package_data=True,
)
