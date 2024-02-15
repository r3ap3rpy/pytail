#!/usr/bin/env python3
with open('pytail/__init__.py') as initfile:
	version = next(iter([ _.strip() for _ in initfile.readlines() if '__version__' in _ ]))

version = version.split(' = ')[-1].replace("'",'')
print(f"Old version {version}")
major, minor, build = version.split('.')
major = int(major)
minor = int(minor)
build = int(build)
print(major,minor,build)
build += 1
if build > 9:
	minor += 1
	build = 0
if minor > 9:
	major += 1
	minor = 0
with open('pytail/__init__.py','w') as initfile:
	initfile.write('from .pytail import *\n')
	initfile.write(f"__version__ = '{major}.{minor}.{build}'\n")
print(major,minor,build)
