Title:Importing Python code by file reference and inspecting classes
Date:08-18-2023
Slug:python-class-inspection

I recently had a use case for importing Python code by reference to its full file path, inspecting each class found within the source, and performing a task if a particular attribute was found. This was for a command-line interface (CLI) and I wanted the script to be run like the following:

`$ python inspect_source.py /full/path/to/source.py`

My initial scan of [stackoverflow answers](https://stackoverflow.com/search?q=import+python+code+and+inspect+classes) didn't provide a solution for exactly what I wanted to do in this case. So I turned to my other favorite resource, [Python 3 Module of the Week](https://pymotw.com/3/index.html), and read up on the standard library's [importlib](https://pymotw.com/3/importlib/index.html) and [inspect](https://pymotw.com/3/inspect/index.html) modules. I was able to piece this together.

--include=content/examples/inspect_source.py

This solution requires that all modules imported by the source file in this case already exist in your environment. Otherwise you will get import errors.