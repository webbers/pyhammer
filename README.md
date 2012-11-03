pyhammer
========
A Python build automation library

Install
-------
Install with [Pip](http://www.pip-installer.org/)

```bash
pip install pyhammer
```

Getting Started
---------------
This library is meant to be a dead simple way to automate your builds. It's inspired in
[Grunt](http://gruntjs.com/) for Javascript. There's a static class called ``Builder`` with
two simple methods ``addTask`` and ``runBuild``.

The method ``addTask`` requires in it's first parameter the name of task. The second
parameter may contain an object inherited from ``TaskBase`` or a string with the previously
added task names separated with spaces.

At the end of file it's necessary put ``Builder.runBuild()``. It starts the build process
search for the first parameter used to call the python file.

Here is a simple example:

```python
from pyhammer.builder import Builder
from pyhammer.tasks.io.copytask import CopyTask
from pyhammer.tasks.io.deletetask import DeleteTask

#Adding the tasks
Builder.addTask('copy', CopyTask('/temp', '/pub'))
Builder.addTask('delete', DeleteTask('/temp'))

#This is a MultiTask that runs 2 previously declared
Builder.addTask('all', 'copy delete')

#This code is required
Builder.runBuild()
```

To execute the file showed above you must call the command below where ``build.py`` is the
name of file and ``all`` is the task you want to run.

```bash
python build.py all
```

## Contributing

Please use the issue tracker and pull requests.

## License
Copyright (c) 2012 Afonso França
Licensed under the MIT license.
