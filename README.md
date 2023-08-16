# GBOmonitoring

This tool can potentially be used as a amalgimation of all the monitoring structures in place for science and software at the Green Bank Observatory. Used as a tool to convey the current or future monitoring efforts to ensure the telescope is running and, impotantly, running correctly.

## Installation

This repo is currently configured to work only with the GBO network, relying on databases and environments available on our internal machines. This can be adapted to outside use if those references are re-configured.

# How to configure GBOmonitoring

Included in this repo are several items: the Monitoring Webpage, <TBD>. To configure all of these, see below.

1.  To get GBOmonitoring

```
    git clone https://github.com/GreenBankObservatory/GBOmonitoring.git
    cd GBOmonitoring
    # make and source a new venv
    ~gbosdd/pythonversions/3.9/bin/python -m venv <path/vevnName>
    source <path/vevnName>/bin/activate
    pip install -U pip setuptools wheel build
    pip install -r requirements.txt
    pip install -e .
```

2.  Set up your environment to access the relevant databases

```
    cp GBOmonitoring/.env.template GBOmonitoring/.env
    # Modify the contents of this file to point to your machine, galileo, etc.
```

3.  Run the website from your development location

```
    # source your venv
    ./manage.py runserver <machine, or 0.0.0.0>:9437
    # then navigate to the webpage on your browser at: <machine>:9437
```