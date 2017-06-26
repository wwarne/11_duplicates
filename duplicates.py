import argparse
import os
from collections import namedtuple
from itertools import combinations

FileInfo = namedtuple('FileInfo', ['name', 'size', 'path'])


def cmp(file1, file2):
    return file1.name == file2.name and file1.size == file2.size


def build_filelist(path):
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for one_file in filenames:
            path = os.path.join(dirpath, one_file)
            info = FileInfo(name=one_file, size=os.path.getsize(path), path=path)
            files.append(info)
    return files


def find_duplicates(filelist):
    duplicates = []
    for file1, file2 in combinations(filelist, 2):
        if cmp(file1, file2):
            duplicates.append((file1, file2))
    return duplicates


def print_duplicates(duplicate_list):
    if not duplicate_list:
        print('Congratulations. You don\'t have duplicates in this directory.')
        return
    for file1, file2 in duplicate_list:
        print('Simular files {} and {}'.format(file1.path, file2.path))


def create_parser():
    result = argparse.ArgumentParser()
    result.add_argument('path', help='Path to a directory')
    return result


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(['z:\\temp'])
    print('Scanning files.')
    all_files = build_filelist(namespace.path)
    print('Finding duplicates.')
    all_duplicates = find_duplicates(all_files)
    print_duplicates(all_duplicates)
