from setuptools import setup

setup(
    name='OpenTypeFeatureLexer',
    version='0.1',
    description='Pygments lexer for OpenType Features',
    author='Frederik Berlaen',
    url='https://github.com/typemytype/OpenTypeFeatureLexer/',
    packages=['openTypeFeatureLexer'],
    entry_points='''[pygments.lexers]
openTypeFeatureLexer = openTypeFeatureLexer:OpenTypeFeatureLexer
'''
)