from setuptools import setup

version = '0.0.1dev'
long_description = '\n\n'.join([
    open('README.md').read(),
    open('CHANGES.md').read(),
])

setup(
    name="daeta",
    version=version,
    description="Datastorage and access from another perspective.",
    long_description=long_description,
    author="Rudy Lattae",
    author_email="rudylattae@gmail.com",
    url='https://github.com/rudylattae/daeta',
    license="MIT",
    keywords=['python', 'daeta', 'data', 'database', 'nosql', 'rdbms', 'schemaless', 'schemaish'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Topic :: Database'
    ],
    py_modules=['daeta'],
    zip_safe=False
)
