#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_hooks_dir():
    return os.path.join(_ROOT, 'hooks')


def main():

    argv = sys.argv

    if len(argv) < 2:
        print 'Usage: git hooks language hook-name'
        exit()

    only_language = False
    if len(argv) == 2:
        only_language = True

    language = argv[1]

    language_path = os.path.join(get_hooks_dir(), language)

    if not os.path.isdir(language_path):
        print 'Not defined hooks for {}'.format(language)
        exit()

    if only_language:
        print 'Hooks available for {}'.format(language)
        for available in os.listdir(language_path):
            print available
        exit()

    hook_name = argv[2]
    hook_path = os.path.join(get_hooks_dir(), language, hook_name)

    if not os.path.isfile(hook_path):
        print 'Not defined {} hook'.format(hook_name)
        exit()

    with open(hook_path) as hook_file:
        print hook_file.read()

if __name__ == '__main__':
    main()
