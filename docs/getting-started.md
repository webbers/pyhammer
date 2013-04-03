Getting Started
===============

Installing PyHammer
-------------------
PyHammer requires Python 3.x and could be installed via [Pip](http://www.pip-installer.org/) a Python package manager. It can be installed downloading and running these Python scripts:

* [http://python-distribute.org/distribute_setup.py](http://python-distribute.org/distribute_setup.py)
* [https://raw.github.com/pypa/pip/master/contrib/get-pip.py](https://raw.github.com/pypa/pip/master/contrib/get-pip.py)

**Note**: You must use sudo (for OSX, Linux etc) or run your command shell as Administrator (for Windows).

After install Pip you still may need register ``<PythonInstallFolder>/Scripts`` in PATH environment variable.

The last step is install pyhammer doing this:
```bash
pip install pyhammer
```

Preparing a new PyHammer project
--------------------------------
A typical setup will involve adding just one file to your project: ``build.js``. It is a valid python file that belongs in the root directory of yout project and should be committed with yout project source.
A build.js is comprised of the following parts:

* Task import area
* Arguments configuration
* Task configuration
* runBuild Command

An example build.py file
------------------------
```python
#Task import area
import os
import sys
import argparse

from pyhammer.builder import Builder
from pyhammer.tasks.io.copytask import CopyTask
from pyhammer.tasks.io.deletetask import DeleteTask

#Arguments configuration
parser = argparse.ArgumentParser()
parser.add_argument( '--build', type=str, required=True )
args = parser.parse_args()

#Task configuration
Builder.addTask( "copy", CopyTask( "src", "pub" ) )
Builder.addTask( "delete", CopyTask( "src" ) )
Builder.addTask( 'default', [ 'copy', 'delete' ])

#runBuild Command
Builder.runBuild(args.build)
```

###Task import area###
It's needed import all tasks I'll use. Remember to call the complete namespace of all tasks you want use

###Arguments configuration###
Here could be created an ``ArgumentParser`` class adding ``--build`` argument

###Task configuration###
Now it's time to configure all tasks. Call the static method ``addTask`` that requires in it's first parameter the name of task. The second parameter may contain an object inherited from ``TaskBase`` or a string with the previously added task names separated with spaces. In this case you'll create a batch of tasks calling.

###runBuild Command###
After configure all tasks, you just need to call static method ``runBuild``. In the first parameter must be placed the name of task to be executed. In case of this sample, we are using build property coming from arguments.

Executing build.py
------------------
To execute the file you must call the command below where ``build.py`` and ``--build=default`` contains the name of task we want to run.

```bash
python build.py --build=default
```
