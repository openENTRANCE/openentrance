# An installable Python package

To facilitate using the definitions in data processing workflows and scripts,
the nomenclature can be installed as a Python package with several utility
functions and dictionaries.

## Documentation

Coming soon - for now, please have a look at [__init__.py](__init__.py)!

## Installation instructions

### Option 1: Clone the repo and install from source (recommended)

This approach requires git to be installed on your machine.

Clone this repository to your machine by opening a command prompt and 
directing it to the folder where you want to have the files, then run:

```
$ git clone git@github.com:openENTRANCE/openentrance.git
```

Then navigate the command prompt to the new folder and install using pip.

```
$ cd nomenclature
$ pip install --editable .
```

> Pulling new commits in the cloned folder will immediately
> make the latest version of the nomenclature available on your machine.

You can test whether the installation worked successfully by running

```
$ pytest openentrance/tests/
```

The result should look similar to the following snippet:

```
============================= test session starts ==============================
platform darwin -- Python 3.7.7, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: ...
collected 4 items                                                              

openentrance/tests/test_core.py ....                                     [100%]

============================== 4 passed in 30.00s ==============================
```
If you see a few warnings, this is (probably) also ok...


### Option 2: Install directly from GitHub

Open a command prompt and run

```
pip install git+https://github.com/openENTRANCE/openentrance
```

> :warning: You will have to repeat this step whenever you want
> to update the `openentrance` package on your machine.
