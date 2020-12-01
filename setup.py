from setuptools import setup, find_packages

setup(
    name='WykazCzasopism',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        find_packages(),
    ],
    entry_points='''
        [console_scripts]
        wykaz=wykaz:cli
    ''',
)
