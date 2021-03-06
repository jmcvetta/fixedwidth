from setuptools import setup

setup(
    name='FixedWidth',
    version='0.99',
    description='Two-way fixed-width / Python dict converter.',
    packages=['fixedwidth',],
    license='BSD',
    url='https://github.com/ShawnMilo/fixedwidth',
    author='Shawn Milochik',
    author_email='shawn@milochik.com',
    zip_safe=False,
    keywords='fixed width',
    test_suite="fixedwidth.tests",
)
