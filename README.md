Whoopsie
===============

'Whoopsie' delete pontentially incriminating evidence -- just like the CIA!

Description
-----------

Write over a file or each file in a directory with a random string of UTF-8 characters equal to the size of the original file an integer number of times before deletion.

Requirements
------------

Python 3.5 or greater

Usage
-----

```
usage: Whoopsie! [-h] [--v] [-r] [-f] Location K

'Whoopsie' delete pontentially incriminating evidence -- just like the CIA!

positional arguments:
  Location        Location of file or directory of files to be Whoopsied
  K               Integer number of passes of random overwrites (default: 5)

optional arguments:
  -h, --help      show this help message and exit
  --v, --version  show version info
  -r, --recurse   recursively delete all files and directories
  -f, --force     force delete -- hide all prompts
```

License
-------

Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
