from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='SampleModule',
    version= '0.0.1',
    author='Sridhar',
    author_email='your@email.com',
    description='This is a Sample Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sridhard/sample_project',
    license='MIT',
    # install_requires=[],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='python package example',
    entry_points={
        'console_scripts': [
            'Endecoder=src.app:main',
        ],
    }
)
