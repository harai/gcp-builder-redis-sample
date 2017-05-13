import setuptools

setuptools.setup(
    name='redis-sample',
    description='Redis Sample',
    long_description='GCP Container Builder Redis Sample',
    url='https://github.com/harai/gcp-builder-redis-sample',
    author='Akihiro HARAI',
    author_email='jharai0815@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Programming Language :: Python :: 3.6',
    ],
    platforms=['linux'],
    packages=['redissample'])
