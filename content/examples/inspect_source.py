import importlib
import inspect
import sys
from pathlib import Path

source_path = sys.argv[1]

cwd = Path(__file__).parent
path = Path(source_path)

module_name = path.stem

# Append the parent of the source_path to the python path
sys.path.append(str(path.parent))
print(f"Importing {source_path} as {module_name}")

# Import the source code as a module.
imported_source = importlib.import_module(module_name)

# Use inspect to get all classes.
for name, _class in inspect.getmembers(imported_source, inspect.isclass):
    # Check for existence of the target attribute.
    try:
        attrib = getattr(_class, "my_target_attribute")
    except AttributeError:
        continue
    if attrib is None:
        continue
    else:
        # If the attribute is found, do something.
        print(f"{name} -- do something with the target attribute.")
