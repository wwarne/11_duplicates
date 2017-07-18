import argparse
import os
from collections import defaultdict


def build_filelist(path):
    files_data = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(path):
        for single_filename in filenames:
            path = os.path.join(dirpath, single_filename)
            files_data[single_filename + str(os.path.getsize(path))].append(path)
    return files_data


def find_duplicates(filelist):
    return [files_list for files_list in filelist.values() if len(files_list) > 1]


def print_duplicates(duplicate_list):
    if not duplicate_list:
        print('Congratulations. You don\'t have duplicates in this directory.')
        return
    for files in duplicate_list:
        print('File `{}` is located at:'.format(os.path.basename(files[0])))
        for file in files:
            print(file)
        print('----')


def create_parser():
    argument_parser = argparse.ArgumentParser(description='File duplicate finder')
    argument_parser.add_argument('path', help='Search in this directory')
    return argument_parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    print('Scanning files in a directory `{}`'.format(namespace.path), end='')
    all_files = build_filelist(namespace.path)
    print(' [OK]')
    print('Searching for duplicates', end='')
    all_duplicates = find_duplicates(all_files)
    print(' [OK]')
    print('-----List of duplicates-----')
    print_duplicates(all_duplicates)