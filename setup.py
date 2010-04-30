from setuptools import setup, find_packages

version = __import__(APP_NAME).__version__

classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Development Status :: 4 - Beta'
]

setup(
    author="Jonas Obrist",
    name="utils",
    version=version,
    url="http://github.com/ojii/django-utils",
    description="Utilities for Django",
    long_description="Utilities for Django",
    platforms=['OS Independent'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Development Status :: 4 - Beta'
    ],
    packages=find_packages(),
    package_dir={
        'utils': 'utils',
    },
    zip_safe = False
)
