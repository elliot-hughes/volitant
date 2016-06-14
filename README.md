# Volitant
Volitant is a Python package that converts and modifies configuration files for an HCAL FE setup.

## Installation
Go to a working directory of your choice and download the code with
```
git clone https://github.com/elliot-hughes/volitant.git
```
If this complains with something like `error: SSL certificate problem, verify that the CA cert is OK.`, you can set `git config --global http.sslVerify false` to ignore it.

## Example
Go into the `volitant` directory and run
```
python convert.py example.xml
```
to convert `example.xml` to `example.txt`.

## Compatibility
This Python package is intended to be compatible with Python 2.4.
