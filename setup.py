from setuptools import setup

setup(
    name='nft_generator',
    version='0.1.0',
    py_modules=['nft_generator'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'nft_generator = nft_generator:cli',
        ],
    },
)