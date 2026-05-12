# Well-Algined Pairs package

This package allows for generating
well-aligned pairs as defined in
[this paper](https://www.math.toronto.edu/vvtewari/richtab.pdf) by Hunter Spink and
Vasu Tewari.

## Package structure

Here is the structure of this very simple SageMath example packa264083ge:

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

    sage: from well_aligned_pairs import WellAlignedPairs
    sage: for p in WellAlignedPairs(3): print(p)
    ╔1 2 3╗
    ╚1 2 3╝
    ╔1 2 3╗
    ╚2 1 3╝
    ╔1 2 3╗
    ╚2 3 1╝
    ╔1 2 3╗
    ╚1 3 2╝
    ╔1 2 3╗
    ╚3 1 2╝
    ╔1 2 3╗
    ╚3 2 1╝
    ╔1 3 2╗
    ╚1 3 2╝
    ╔1 3 2╗
    ╚3 1 2╝
    ╔2 1 3╗
    ╚2 1 3╝
    ╔2 1 3╗
    ╚2 3 1╝
    ╔2 1 3╗
    ╚3 1 2╝
    ╔2 1 3╗
    ╚3 2 1╝
    ╔2 3 1╗
    ╚2 3 1╝
    ╔2 3 1╗
    ╚3 2 1╝
    ╔3 1 2╗
    ╚3 1 2╝
    ╔3 1 2╗
    ╚3 2 1╝
    ╔3 2 1╗
    ╚3 2 1╝
    sage: for p in WellAlignedPairs(3, u=[2,1,3]): print(p)
    ╔2 1 3╗
    ╚2 1 3╝
    ╔2 1 3╗
    ╚2 3 1╝
    ╔2 1 3╗
    ╚3 1 2╝
    ╔2 1 3╗
    ╚3 2 1╝

## Check that all tests pass in the package

Check the c╔2 1 3╗
╚2 1 3╝
╔2 1 3╗
╚2 3 1╝
╔2 1 3╗
╚3 1 2╝
╔2 1 3╗
╚3 2 1╝
overage of functions in the package. To get 100% coverage, every
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

To do: doctests
╔2 1 3╗
╚2 1 3╝
╔2 1 3╗
╚2 3 1╝
╔2 1 3╗
╚3 1 2╝
╔2 1 3╗
╚3 2 1╝

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
