# Workflow in my research
In a research project, there are multiple programming, simulation and writing tasks. Therefore, it is necessary to streamline the workflow to accelerate my research.

## Python development
**Python** is my primary programming language for analysis code and quick model implementation. For my typical workload, lightweight **Visual Studio Code** is a decent choice of development environment.
### Environment management
It is always a good idea to isolate **Python** environment where thirdparty packages are installed. Several options are available, however, I prefer to use the built-in **venv** module due to its simplicity. On **macOS** with brand new **Apple Silicon**, **numpy** has kind of performance issue since the absence of **MKL** library and a possible fix is by using **conda** and leveraging Apple's **Accelerate** library (see [issue](https://github.com/conda-forge/numpy-feedstock/issues/253)). However, after my own [experiment](https://github.com/tim939422/python_apple_silicon), the performance different is not significant enough and I will stay with **venv**. It is pretty straightforward to install packages inside a virtual environment via **pip** but the only two remarks are made here:
    
1. use module method instead of the command itself, i.e., 

    `python -m pip install <package name>`

    instead of

    `pip install <package name>`
    
2. upgrade **pip** first:
    
    `python -m pip install --upgrade pip`

A environment is portable by creating a `requirements.txt`
```
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```
Since I use only a small collection of packages,

- numpy
- scipy
- pandas
- scikit-learn
- matplotlib
- notebook
- pytest

This file is provided in this template repo for quick start.
### Configure Visual Studio Code

## Thirdparty codes
I have been a big fan of conda for years. However, I switch to `venv` recently. The python is installed by apt and `python3.8-venv` must be installed.
```shell
sudo apt install python3.8 python3.8-venv
```
For individual project, a virtual environment must be created, activated and upgraded.
```shell
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```
and select the proper interpreter in vscode by `Python: Select Interpreter`. Since venv hardcodes the shebang line, the virtual environment is not portable across different folder and platform. A `requirements.txt` will be used to reproduced the developement environment by
```shell
python -m pip freeze > requirements.txt # create
python -m pip install -r requirements.txt # setup
```
## My own codes
Common functions are organized in packages located in `${workspaceFolder}/src` for convenient reuse. However, it is nasty to configure Python search path in visual studio code. I find this [discussion](https://stackoverflow.com/questions/53653083/how-to-correctly-set-pythonpath-for-visual-studio-code) pretty useful. To make start debugging work, add the following line to `${workspaceFolder}/.vscode/launch.json`
```json
"env": {"PYTHONPATH": "${workspaceFolder}/src"}
```
. This will actually append `PYTHONPATH` with specified value, therefore, the search configured before entering vscode will be untouched. Two remarks must be made here,
1. Shortcuts `F5` (Start Debugging) and `Ctrl+F5` (Run Without Debugging) is functional keys on my current keyboard and I also need to hold `fn` key.
2. The environment variable will not have an affect on `Run Python File` and `Debug Python File`, i.e., they will not work at all. To make life easier, I will insist on the former way at least for code development.
For jupyer notebooks, an ugly way is adopted now, i.e., add this cell at the beginning of every notebook
```python
%matplotlib inline
# thirdparty packages
import matplotlib.pyplot as plt
import numpy as np

# local development
import sys
sys.path.append('<absolute path to package root (src)>')
from package_a import foo
```

## Unit testing


# Reference management
Obsidian to take notes