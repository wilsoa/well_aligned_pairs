# Well-Algined Pairs package

This package allows for generating
well-aligned pairs as defined in
[this paper](https://www.math.toronto.edu/vvtewari/richtab.pdf) by Hunter Spink and
Vasu Tewari.

## Package structure

Here is the structure of this very simple SageMath example package:

    ├── well_aligned_pairs
    │   ├── __init__.py
    │   └── main.py
    ├── .gitignore
    ├── README.md
    ├── VERSION
    ├── makefile
    └── pyproject.toml

## Installation

To install the most recent development version:

    sage -pip install --upgrade git+https://github.com/wilsoa/well_aligned_pairs

or from within sage,

`   %pip install --upgrade git+https://github.com/wilsoa/well_aligned_pairs`

## Usage

Open sage:

    $ sage

Use it:

    sage: import simple_sagemath_package
    sage: simple_sagemath_package.hello()
    Hello from my new package!

Use a function in the package that depends on SageMath:

    sage: from simple_sagemath_package import print_charpoly_of_a_random_matrix
    sage: print_charpoly_of_a_random_matrix()
    Here is a random 3 x 3 matrix:
    [  1   2  -1]
    [ -4 -33  -4]
    [  1  -5  -1]
    Here is its characteristic polynomial:
    x^3 + 33*x^2 - 12*x + 56

    sage: print_charpoly_of_a_random_matrix()
    Here is a random 3 x 3 matrix:
    [ -1   1   1]
    [  1 557   0]
    [ -1   0  -3]
    Here is its characteristic polynomial:
    x^3 - 553*x^2 - 2225*x - 2231

## Check that all tests pass in the package

Check the coverage of functions in the package. To get 100% coverage, every
function needs to be documented *and* that documentation must contain examples.
These are called *doctests*.

    $ make coverage
    sage -coverage simple_sagemath_package/*
    ------------------------------------------------------------------------
    No functions in simple_sagemath_package/__init__.py
    ------------------------------------------------------------------------
    SCORE simple_sagemath_package/main.py: 100.0% (2 of 2)
    ------------------------------------------------------------------------

Test all doctests of the package:

    $ make test
    mkdir -p logs
    sage -t --force-lib --log=logs/test.log simple_sagemath_package demos
    Running doctests with ID 2026-05-05-17-42-47-e7678fd1.
    Doctesting 2 files.
    sage -t --warn-long 5.0 --random-seed=72057821218394581103186403749166067443 simple_sagemath_package/main.py
    **********************************************************************
    File "simple_sagemath_package/main.py", line 17, in simple_sagemath_package.main
    Failed example:
        3 + 4
    Expected:
        34
    Got:
        7
    **********************************************************************
    1 item had failures:
       1 of   4 in simple_sagemath_package.main
        [8 tests, 1 failure, 0.01s wall]
    sage -t --warn-long 5.0 --random-seed=72057821218394581103186403749166067443 simple_sagemath_package/__init__.py
        [0 tests, 0.00s wall]
    sage -t --warn-long 5.0 --random-seed=37448503971169684617593550135978003287 demos/arXiv_2604_20964.rst
        [4 tests, 0.01s wall]
    ----------------------------------------------------------------------
    sage -t --warn-long 5.0 --random-seed=72057821218394581103186403749166067443 simple_sagemath_package/main.py  # 1 doctest failed
    ----------------------------------------------------------------------
    Total time for all tests: 0.0 seconds
        cpu time: 0.0 seconds
        cumulative wall time: 0.0 seconds
    Features detected for doctesting:
    make: *** [makefile:12 : test] Erreur 1

Oups, one doctest out of 12 is currently broken. We should fix it! The broken
test are listed in `logs/test.log`.

## Distribute this package

Build the package:

    $ sage -python -m build -s
    * Creating isolated environment: venv+pip...
    * Installing packages in isolated environment:
      - setuptools >= 40.8.0
    * Getting build dependencies for sdist...
    * Building sdist...
    Creating tar archive
    removing 'simple_sagemath_package-0.1.0' (and everything under it)
    Successfully built simple_sagemath_package-0.1.0.tar.gz

The package is now available in the `dist` folder:

    $ ls dist/
    simple_sagemath_package-0.1.0.tar.gz

You may now upload this file on your website for other people to install and
use it. For example, the following command would allow them to install it:

    $ sage -pip install simple_sagemath_package-0.1.0.tar.gz
    $ sage -pip install https://your.website.com/simple_sagemath_package-0.1.0.tar.gz

## For more information

For more information on how to make a Python Package, please visit the [official
latest documentation](https://packaging.python.org/en/latest/).

The webpage [Python packages with pyproject.toml and nothing
else](https://til.simonwillison.net/python/pyproject) by Simon Willison was
useful for preparing this example.

I also strongly recommend reading the [Best Practices for Scientific
Computing ](https://doi.org/10.1371/journal.pbio.1001745) which you want to
apply when constructing your future package.

Make sure you follow the [SageMath coding conventions](https://doc.sagemath.org/html/en/developer/coding_basics.html) both for the code and for documentation. This will make it easier to
be merged into SageMath one day. In particular, documentation of every modules,
classes, methods and functions is using the [ReStructuredText
syntax](https://docutils.sourceforge.io/docs/user/rst/quickref.html) which is
good to learn.

Once your package is ready, you may want to share it on the official [Python
Package Index](https://pypi.org/).

To make a more complicated package for example involving Cython code and
including auto-generated documentation, please visit how other SageMath
packages are made, for example, the following two:

 - https://pypi.org/project/sage-flatsurf/
 - https://pypi.org/project/slabbe/
