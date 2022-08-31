# ransom-files-generator
Python script to generate random files to perform a ransomware simulation using Infection Monkey

```
usage: generator.py [-h] [-p PATH] [-n FILES] [-f FOLDERS] [-d DEPTH] [-r REPEAT]

Generate random files for Infection Monkey Ransomware

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  path/to/basedir
  -n FILES, --files FILES
                        number of files per folder
  -f FOLDERS, --folders FOLDERS
                        number of folders
  -d DEPTH, --depth DEPTH
                        max depth of folders
  -r REPEAT, --repeat REPEAT
                        times to walk over created files and directories
```