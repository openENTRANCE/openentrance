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
$ git clone git@github.com:openENTRANCE/nomenclature.git
```

Then navigate the command prompt to the new folder and install using pip.

```
$ cd nomenclature
$ pip install --editable .
```

> :warning: Pulling new commits in the cloned folder will immediately
> make the latest version of the nomenclature available on your machine.

### Option 2: Install directly from GitHub

Open a command prompt and run

```
pip install git+https://github.com/openENTRANCE/nomenclature
```

> You will have to repeat this step whenever you want
> to update the `nomenclature` package on your machine.

### Known issues

The `nomenclature` Python package requires
the [pyam](https://pyam-iamc.readthedocs.io) package
and installing as indicated above will automatically install **pyam**
from [pypi](https://pypi.org/project/pyam-iamc/).

However, some operating systems have dependency conflicts between **pyam**
and **pypi** - if you experience any problems, please try to install
with conda using

```
conda install -c conda-forge pyam
```
