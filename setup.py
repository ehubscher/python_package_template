from setuptools import setup, find_namespace_packages

setup(
    name='namespace_name_package_name',
    version='0.1.0',
    packages=find_namespace_packages(),
    author='Your Name',
    author_email='your.name@example.com',
    description='This is an example description for this package.',
    license='',
    keywords='example key words for this package',
    project_urls={'Source Code': 'https://github.com/your.name/namespace_name_package_name'},
    install_requires=[
        'dependency1',
        'dependency2'
    ]
)
