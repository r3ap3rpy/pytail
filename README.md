### Welcome

This is a repository that holds my implementation of the **tail -f** command.

In order to install it you can use either of these two ways.

``` bash
git clone https://github.com/r3ap3rpy/pytail
cd pytail
python setup.py install
```

OR

``` python
pip install pytail-r3ap3rpy
```

There are two arguments:
- file (The file you want to tail!)
- filter (Optional, allows you to get only lines that contain the filter, case-insensitive!)

## ToDo
- [ ] Add automatic version bump to workflow
- [x] Add permission check to see if user has the right to read the file!
- [x] Change it to use **argparse**
- [x] Add versioning
- [x] Add switches

