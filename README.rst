AlgoPy
=========

.. image:: https://travis-ci.org/kskrishnasangeeth/AlgoPy.svg?branch=master
   :target: https://travis-ci.org/kskrishnasangeeth/AlgoPy

.. image:: http://img.shields.io/codecov/c/github/kskrishnasangeeth/AlgoPy.svg?style=flat
   :target: https://codecov.io/github/kskrishnasangeeth/AlgoPy?branch=master

.. image:: https://readthedocs.org/projects/AlgoPy/badge/?version=latest
   :target: https://readthedocs.org/projects/AlgoPy/?badge=latest
   :alt: Documentation Status


The idea behind this project is to solve Algorithm problems and puzzles
in Python by following TDD and good programming guidelines such as using
docstring , checking for PEP8 violations etc.

The key goal here is to learn by solving some of these problems yet at the
same time write clean and elegant code. The problems are curated from 
sources like GeekforGeeks , hackerrank, SPOJ etc. Check out the issues for 
the current list of problems.
 
The inspiration for this project comes from `Libcipher 
<http://www.github.com/chennaipy/libcipher>_` a project which I was lucky to participate 
as part of initiative by the Chennai Python user group 
which taught me a good deal in python best practices.
 

Development
-----------

After cloning the repository, install the package in development mode
using the following command ::

  $ python3 setup.py develop

You can execute the unit tests, using the following command ::

  $ python3 setup.py test

You can build the documentation, using the following commands ::

  $ pip install -r doc-requirements.txt
  $ cd doc
  $ make html

Contributing Guidelines
-----------------------

Before sending a pull request, please ensure the following:

* The code has been checked for `PEP8
  <https://www.python.org/dev/peps/pep-0008/>`_ compliance using the
  ``pep8`` tool.

* Unit test cases have been added for the new functionality, and the
  line coverage is 100%.

* Docstrings have been added to public functions, that they adhere to
  `Google Docstring Convention
  <https://google-styleguide.googlecode.com/svn/trunk/pyguide.html>`_.

* The API manual has been updated, to display the documentation for
  any new modules added.

* The changelog has been updated, to indicate the change made along
  with the issue no. on GitHub. The changelog is to be in `releases
  format <http://releases.readthedocs.org/en/latest/index.html>`_.
