# GBOmonitoring

This tool can potentially be used as a amalgimation of all the monitoring structures in place for science and software at the Green Bank Observatory. Used as a tool to convey the current or future monitoring efforts to ensure the telescope is running and, impotantly, running correctly.

## Getting Started
### Installation

WOAH requires Python 3.11+. To install from github without creating a separate virtual environment:

```bash
    $ git clone git@github.com:GreenBankObservatory/GBOmonitoring.git
    $ cd GBOmonitoring
    $ pip install -e .
```
If you wish to install using a virtual environment, which we strongly recommend if you plan to contribute to the code, see Development.

### Reporting Issues

If you find a bug or something you think is in error, please report it on
the [github issue tracker](https://github.com/GreenBankObservatory/GBOmonitoring/issues).
(You must have a [Github account](https://github.com) to submit an issue)

## Development

Here are the steps if you want to develop code for WOAH. We use [hatch](https://hatch.pypa.io/) to manage the build environment. The usual caveats apply how you set up your Python development environment.

1.  Clone the repo and install hatch.

```bash
    $ git clone git@github.com:GreenBankObservatory/GBOmonitoring.git
    $ cd GBOmonitoring
    $ pip install hatch
```

2.  Hatch will default to using the system Python if there's no ``HATCH_PYTHON`` environment variable set. To use a specific version of Python, add the following line to your ``~/.bash_profile``:

```bash
export HATCH_PYTHON=/path/to/bin/python
```

Then source the new profile to apply the changes.

```bash
$ source ~/.bash_profile
```

3.  Create and activate a virtual environment with hatch and install the packages required for development. 
The virtual environment will be created the first time; subsequent invoking ``hatch shell`` will simply load the created environment.cdi

```bash
    $ hatch shell
    (woah) $ pip install -r requirements.txt
```

4.  Build and install the package

```bash
    (woah) $ hatch build
    (woah) $ pip install -e .
```

5.  You can exit this environment (which effectively had started a new shell) just exit:

```bash
    (woah) $ exit
```

6.  Each time when you come back in this directory without being in this virtual environment, you'll need to load the virtual environment

```bash
    $ hatch shell
```

Notice you can ONLY do that from this directory

## Testing
We use ``pytest`` for unit and integration testing.  From the top-level GBOmonitoring directory, run:

```bash
    $ pytest
```