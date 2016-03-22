#!/usr/bin/env python2.7
from __future__ import print_function

from collections import defaultdict
from os          import path
import re
import subprocess
import sys

def get_ftype(fpath):
    _, ext = path.splitext(fpath)
    if not ext:
        # No extension; look at the first line
        with open(fpath) as f:
            first_line = f.readline()
            if re.search(r'^#!.*\bpython', first_line):
                return '.py'
            elif re.search(r'^#!.*sh', first_line):
                return '.sh'
            elif re.search(r'^#!.*\bperl', first_line):
                return '.pl'
            elif re.search(r'^#!', first_line):
                print('Error: Unknown shebang in file "%s":\n%s' % (fpath, first_line), file=sys.stderr)
                return ''
            else:
                return ''

    return ext

def list_files(args, modified, exclude_files=[], exclude_trees=[]):
    if modified:
        # If the user specifies, use `git ls-files -m` to only check modified, non-staged
        # files in the current checkout.  This makes things fun faster.
        files = list(map(str.strip, subprocess.check_output(['git', 'ls-files', '-m']).split('\n')))
    else:
        files = []

    files += args

    if not files and not modified:
        # If no files are specified on the command line, use the entire git checkout
        files = list(map(str.strip, subprocess.check_output(['git', 'ls-files']).split('\n')))

    files = list(filter(bool, files)) # remove empty file caused by trailing \n

    if not files:
        raise Exception('There are no files to check!')

    # Categorize by language all files we want to check
    by_lang   = defaultdict(list)

    for fpath in files:
        if (not fpath or not path.isfile(fpath)
            or (fpath in exclude_files)
            or any(fpath.startswith(d+'/') for d in exclude_trees)):
            continue

        try:
            filetype = get_ftype(fpath)
        except (OSError, UnicodeDecodeError) as e:
            etype = e.__class__.__name__
            print('Error: %s while determining type of file "%s":' % (etype, fpath), file=sys.stderr)
            print(e, file=sys.stderr)
            filetype = ''

        by_lang[filetype].append(fpath)

    return by_lang
