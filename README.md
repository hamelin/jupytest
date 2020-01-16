# `jupytest` -- Writing unit and integration tests in a Jupyter notebook

You like the super-short try-until-succeed development cycle that comes from
implementing code in a Jupyter notebook? You would also like to perform your
development with a bit of discipline, writing repeatable unit and integration
tests as you go? This Python package is for you.

You can start your notebook by instantiating a test suite, and as you
test-driven-develop your code (or something), you add tests to that suite.
These tests are run as you go. The test suite accumulates your test results
and can produce a report at the end. The package also includes an executable
script that will take your notebook of tests as input, run it all from the
command line, and write a nice result report to the shell -- or some raw test
result data structure, if that's how you fly.

## Install

```
pip install jupytest
```


## Getting started

![jupytest example involving a typo in an axpy
implementation](examples/axpy.png)

In a nutshell:

1. Import `jupytest`
1. Instantiate the `Suite` class to get a test suite object.
    1. Use the `Report` plug-in at instantiation to get immediate feedback as
       tests are run.
1. For each test to implement, use method `test("<name of the test")` as a
   context manager, and implement the text under the `with` statement.
1. Use any of the functions `report_results`, `summarize_results` or
   `detail_results` to produce the test results to some chosen level of
   detail regarding which tests have been run (and how often), which problems
   have been encountered, and tracebacks of the issues.

The environment of each test is isolated, as if it were written as a function
(except when this isolation is explicitly disabled). Any test can be run more
than once, and the results of each test run are captured in the suite object.

A full example is provided as a [flawed
implementation](examples/fizzbuzz.ipynb) of the classical FizzBuzz problem.


## Further documentations

All the classes and routines of the package are documented with docstrings.
Import `jupytest` in a notebook, then run `jupytest?` to get an index.


## Development

The whole package is implemented through notebook
[`jupytest.ipynb`](jupytest.ipynb). The unit and integration tests of the
package are inline to this notebook. Its full execution renders the module file
`jupytest.py` that is packaged for distribution through PyPI and convenience
of importation.

The packages `jupytest` depends on for its usage are set up directly in the
[`setup.py`](setup.py) script; the development dependencies are in
[`requirements_dev.txt`](requirements_dev.txt). To set oneself up for opening
the Jupytest notebook, run from a shell the following two commands:

```
pip install -r dev/requirements.txt
pip install -e .
```
