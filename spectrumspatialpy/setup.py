from setuptools import find_packages, setup

setup(name='spectrumspatialpy',
      version='0.1',
      description='Client integration of Spectrum Spatial for Python',
      url='https://github.com/Precisely/spectrumpy',
      author='Cary Peebles',
      author_email='cary.peebles@precisely.com',
      license='Apache License 2.0',
      packages=find_packages("src"),
      package_dir={"": "src"},
      install_requires=[
            'spectrumpy',
            'pandas',
            'geopandas',
            'colour',
            'datetime'
      ],
      zip_safe=False)
