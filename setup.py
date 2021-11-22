from setuptools import setup

setup( name='PlotKM',
       version='0.01',
       author='Kyle Mills',
       author_email="kyle.mills@uoit.net",
       description="Set matplotlib style to conform with Kyle Mills' style",       packages=['plotkm'],
       install_requires=['matplotlib>=3.1.0'],
       include_package_data=True
    )
