from setuptools import setup, find_packages


setup(
    name='testprj_Python_aSimple',
    author='Jason beach',
    author_email='jason.beach@mgmt-tech.org',
    description='Simple test code for python language to be run against ScrumSaga.com',
    license='MIT',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['argparse'],
    entry_points={
        'console_scripts': [
            'aSimple=aSimple.__main__:main'
        ]
    }
)
