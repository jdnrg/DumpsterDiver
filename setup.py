from setuptools import setup, find_packages


setup(name='DumpsterDiver',
      version="git-5a291cd",
      py_modules=["advancedSearch","core","DumpsterDiver","entropy"],
      install_requires=[
          'termcolor==1.1.0',
          'passwordmeter==0.1.8',
          'PyYAML==5.1',
      ]
)
