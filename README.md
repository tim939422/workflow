In a research project, there are multiple programming, simulation and writing tasks. Therefore, it is necessary to streamline the workflow to accelerate my research. A typical project layout is like this:

```shell
.
├── data
├── notebooks
├── README.md
├── references
├── scripts
└── src
```

# Python development
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
# Reference management