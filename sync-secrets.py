#!/usr/bin/env python3

import os
import shutil
import sys
import argparse

BACKUP_ROOT = '/tmp'

def backup_secrets(filename):
    project_path = os.getcwd()[1:].split('/')

    if project_path[0] == 'home':
        del project_path[0:2]

    backup_path = BACKUP_ROOT + '/' + '/'.join(project_path)

    source_path = None
    if '/' in filename:
        source_path = filename.split('/')
        source_path = '/'.join(source_path[:-1])

    os.makedirs(backup_path, exist_ok=True)
    new_file = backup_path +  '/' + filename

    print('Saved file: ', new_file)

    shutil.copy(filename, new_file)


if __name__ == '__main__':
    arg_files = sys.argv[1:]

    if len(arg_files) == 0:
        print('usage: sync-secrets file1.txt [file2.txt]')
        sys.exit()
    elif len(arg_files) > 1:
        for arg in arg_files:
            backup_secrets(arg)
    else:
        backup_secrets(arg_files[0])
