from setuptools import setup, find_packages

name = "demo"
version = "0.1"

dependency_links=[
]

setup(
    name=name,
    version=version,
    description="demo",
    long_description='',
    classifiers=[],
    keywords="",
    author="",
    author_email='',
    url='',
    license='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    dependency_links=dependency_links,
    install_requires=[
        'markdown',
        'balanced',
    ],
)
