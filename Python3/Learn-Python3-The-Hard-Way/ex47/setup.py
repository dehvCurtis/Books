try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'',
    'author':'My Name',
    'url':'URL',
    'download_url':'Where to download',
    'author_email':'My email',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)