from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Predict whether a patient will be readmitted within 30 days based on their lab results, medications, and time in hospital.',
    author='Ritam Rakshit',
    license='MIT',
)
