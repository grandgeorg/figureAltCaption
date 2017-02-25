#! /usr/bin/env python


from setuptools import setup
setup(
    name='mdx_figurealtcaption',
    version='1',
    author='Jan Dittrich',
    author_email='d _ jan AT ymail.com',
    description='Generates a figurecaption each Image which stands alone in a paragraph',
    url='https://github.com/grandgeorg/figureAltCaption',
    py_modules=['figureAltCaption'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 1',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE Version 2',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)