from setuptools import setup

setup(
  name = 'loopfield',
  packages = ['loopfield'],
  version = '1.0.2',
  description = 'Current loop magnetic field calculator',
  author = 'Ted Yapo',
  author_email = 'ted.yapo@zednaughtlabs.com',
  url = 'http://github.com/tedyapo/fieldloop',
  classifiers = ['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3',
                 'Operating System :: OS Independent',
                 'Development Status :: 3 - Alpha',
                 'Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Visualization'],
  install_requires = [
    'numpy',
    'scipy',
    'matplotlib >= 1.5.1']
)
