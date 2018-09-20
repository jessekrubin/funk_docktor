# -*- coding: utf-8 -*
import inspect
from os import *

before_path = path.join(getcwd(), 'before.py')
import docktor_before

print(before_path)
a = dir(docktor_before)
print(a)
from itertools import count


def _line_doctor(line):
    """takes a line
    looks for a pattern
    returns indents/spaces, start of pattern
    """
    first = line.find('#')
    if first > -1 and line[first + 2] == '#':
        for i in range(first, 0, -1):
            if line[i] != ' ':
                return line[:i - 1], line[first:]
    # return None, None
    return None


def format_line(code, comment, maxlen):
    """Format a single line

    :param code:
    :param comment:
    :param maxlen:
    :return:
    """
    return code + '  ' + ' ' * (maxlen - len(code)) + comment

def funk_docktor(fname, funk):
    lines, iline_no = inspect.getsourcelines(funk)
    codes = []
    comments = []
    for iline in range(len(lines)):
        doct = _line_doctor(lines[iline])
        if doct is not None:
            code, comment = _line_doctor(lines[iline])
            codes.append(code)
            comments.append(comment)

    mlen = max(len(code) for code in codes)
    formed = []
    for i in range(len(codes)):
        if comments[i] is None:
            # formed.append('\n')
            # formed.append('\n')
            formed.append(lines[i])
        else:
            formed.append(format_line(codes[i], comments[i], mlen))
    print('\n__BEFORE__')
    print(''.join(lines))
    print('__AFTER__')
    print(''.join(formed))
    print("")
    print("")
    print("")

    # mfirst = max(firsts)+2


funks = inspect.getmembers(docktor_before, inspect.isfunction)
print(funks, type(funks))

for name, f in funks:
    funk_docktor(name, f)

print(inspect.getcomments(docktor_before))

# def readin(fpath):
# ins.

# print(inspect.getmembers(before_path, [inspect.isfunction, inspect.iscode]))

#
# if __name__ == '__main__':
#     import argparse
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                         action="store_true")
#     args = parser.parse_args()
#     if args.verbose:
#         print
#         "verbosity turned on"
