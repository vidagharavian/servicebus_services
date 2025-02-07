from setuptools import setup, find_packages

setup(
    name='logix_servicebus_service',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[],  # List dependencies here if any
    author='Vida_gh',
    author_email='vgharavian@logixits.com',
    description='this library is designed to send and receive messages from azure service bus',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vidagharavian/servicebus_services.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)