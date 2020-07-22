import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
  name = 'pymonics',
  packages = ['pymonics'],
  version = '0.1',
  license='MIT',
  description = 'A Powersystems harmonic estimation and filter design package for Python',   
  author = 'Venkatesh Pampana & Ankit Srivastava',
  author_email = 'venkatmr.perfect@gmail.com',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com/ECOWET-Toolset/Pymonics',
  keywords = ['harmonics', 'power systems', 'harmonic filters','low-pass filter','high-pass filter','Memo'],
  install_requires=[ 
          'pandas',
          'numpy',
		  'scipy',
      ],
  classifiers=[
    'Development Status :: 4 - Beta', 
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)