pi = 3.142

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

import sys
import pathlib
parent = pathlib.Path(__file__).parent.parent
sys.path.append(str(parent))
from dir2.calc2 import const


# print(const)











import importlib.util
import sys
from pathlib import Path

def import_custom_module(module_name, path):
    module_path = Path(path) / module_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    print(sys.modules)
    return module


my_module = import_custom_module("calc2.py", str(Path(__file__).parent.parent)+"/dir2")

print(my_module.const)
