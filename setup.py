from setuptools import setup, find_packages

setup(
    # Name called at cl
    name='ttrpg',
    version='0.1',
    # Packages to include
    packages=find_packages(),
    include_package_data=True,
    # Dependencies
    install_requires=[
    ],
    # Entry
    entry_points={
        'console_scripts': [
            'ttrpg=ez_ttrpg.cli:main',
        ],
    },
    # Metadata
    author='Matthew Ghere',
    description='A simple tool for managing TTRPG campaigns',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mrg327/ez-ttrpg',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

