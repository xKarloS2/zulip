#!/usr/bin/env python2.7
from __future__ import print_function

from collections import defaultdict
from os          import path
import re
import subprocess
import sys

def get_ftype(filepath):
    _, exn = path.splitext(filepath)
    if not exn:
        # No extension; look at the first line
        with open(filepath) as f:
            first_line = f.readline()
            if re.match(r'^#!.*\bpython', first_line):
                exn = '.py'

    return exn

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

    for filepath in files:
        if (not filepath or not path.isfile(filepath)
            or (filepath in exclude_files)
            or any(filepath.startswith(d+'/') for d in exclude_trees)):
            continue

        try:
            filetype = get_ftype(filepath)
        except (OSError, UnicodeDecodeError) as e:
            etype = e.__class__.__name__
            print('Error: %s while determining type of file "%s":' % (etype, filepath), file=sys.stderr)
            print(e, file=sys.stderr)
            filetype = ''

        by_lang[filetype].append(filepath)

    by_lang['.sh'] = [_f for _f in map(str.strip, subprocess.check_output("grep --files-with-matches '#!.*\(ba\)\?sh' $(git ls-tree --name-only -r HEAD scripts/ tools/ bin/ | grep -v [.])", shell=True).split('\n')) if _f]

    return by_lang
