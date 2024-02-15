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

## Usage

Simply specify the file or filter to use the tool.

``` bash
╰─>$ pytail --file test.txt
##############################
# Tailing file: test.txt
# Use <CTRL + C> to exit
##############################
2024-02-15 13:42:35.747232 :: line
2024-02-15 13:42:40.425967 :: another
2024-02-15 13:42:44.374841 :: yet another
##############################
# End of tailing!
# Elapsed time: 15.93 second(s)!
# Speed: 0.19 lps (lines per second)
##############################
```

## Notes

If you install it in a virtualenv it will just work fine!

On MacOS systems the module works fine.

On linux systems if you install the module with **sudo** it will work fine, if you install it without **sudo** you may have to issue the following command after install if you cannot find the **pytail** executable.

``` bash
export PATH="$HOME/.local/bin:$PATH"
```

There are two arguments:
- file (The file you want to tail!)
- filter (Optional, allows you to get only lines that contain the filter, case-insensitive!)

## ToDo
- [ ] Check install issues!
- [x] Add automatic version bump to workflow
- [x] Add permission check to see if user has the right to read the file!
- [x] Change it to use **argparse**
- [x] Add versioning
- [x] Add switches

