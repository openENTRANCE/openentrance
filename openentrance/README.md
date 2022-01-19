# An installable Python package

To facilitate using the definitions in data processing workflows and scripts,
the nomenclature can be installed as a Python package with several utility
functions and dictionaries.

## Documentation

Coming soon - for now, please have a look at [__init__.py](__init__.py)!

## Installation instructions

### Clone the repo and install from source

This approach requires git to be installed on your machine.

Clone this repository to your machine by opening a command prompt and 
directing it to the folder where you want to have the files, then run:

```
$ git clone git@github.com:openENTRANCE/openentrance.git
```

Then navigate the command prompt to the new folder and install using pip.

```
$ cd openentrance
$ pip install -r requirements.txt
$ pip install --editable .
```

> Pulling new commits in the cloned folder will immediately
> make the latest version of the nomenclature available on your machine.

You can test whether the installation worked successfully by install **pytest** using

```
$ pip install pytest
```

and then running

```
$ pytest openentrance/tests/
```

The result should look similar to the following snippet:

```
============================= test session starts ==============================
platform darwin -- Python 3.9.7, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
collected 20 items                                                             

tests/test_core.py ..                                                    [ 10%]
tests/test_definitions.py ......                                         [ 40%]
tests/test_validate.py ............                                      [100%]

============================= 20 passed in 40.83s ==============================
```

If you see a few warnings, this is (probably) also ok...
