from setuptools import setup, find_packages

requires = [
    'fastapi',
    'uvicorn'
    #'psycopg2',
]

setup(
    name='fastapi_test',
    version='0.0',
    description='Hello world FastAPI',
    author='Arizon',
    author_email='arizon.es@gmail.com',
    keywords='web FastAPI',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
