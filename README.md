### Welcome

This is a repository that holds my implementation of the **tail -f** command.

In order to install it you can use either of these two ways.

``` bash
git clone
cd pytail
python setup.py install
```

OR

``` python
pip install pytail
```

There are two arguments:
- file (The file you want to tail!)
- filter (Optional, allows you to get only lines that contain the filter, case-insensitive!)

## ToDo
- [x] Change it to use **argparse**
- [x] Add versioning
- [x] Add switches
