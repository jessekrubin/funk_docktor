# -*- coding: utf-8 -*
from itertools import chain
from os import getcwd, path
import argparse
from pupy.decorations import tictoc

CD = getcwd()

def fmt_line(line, col, phillup=False):
    """

    :param line:
    :param col:
    :return:

    # >>> format_line([])
    """
    if len(line) == 1:
        code = line[0]
        if phillup: return ''.join((code, ' ' * (1 + col - len(code)), '#$#'))
        else: return code
    if len(line) == 2:
        code, comment = line
        return ''.join((code, ' ' * (1 + col - len(code)), '#$#', comment))

@tictoc()
def funk_docktor(unfunky, clusters=True, phillup=False):
    """Formats a multi-line string"""
    if clusters:
        pass
    else:
        lines = unfunky.replace('# $#', '#$#').split('\n')
        furst = min(i for i, line in enumerate(lines)
                    if '#$#' in line)
        last = max(i for i, line in enumerate(lines)
                   if '#$#' in line)
        doc_lines = [line.split("#$#")
                     for line in lines[furst:last + 1]]
        maxcodelength = max(len(line[0]) for line in doc_lines
                            if len(line) == 2)
        lgne = [fmt_line(line,
                         col=maxcodelength,
                         phillup=phillup)
                for line in doc_lines]
        if phillup and doc_lines[-1][0] == '':
            lgne[-1] = ''

        return '\n'.join(chain.from_iterable((lines[:furst], lgne, lines[last + 1:])))

def main():
    parser = argparse.ArgumentParser(description='~ ~ ~ Funk ~ DOCKTOR ~ ~ ~ ')
    parser.add_argument('-p', '--phillup',
                        action="store_true",
                        dest='phillup',
                        default=False)
    parser.add_argument('-i', '--inplace',
                        action="store_true",
                        dest='inplace',
                        default=False)
    parser.add_argument('-f', '--file',
                        type=argparse.FileType('r'),
                        nargs='+')

    args = parser.parse_args()
    for file in args.file:
        abs_fpath = path.join(CD, file.name)
        fdir, fname = path.split(abs_fpath)
        fname = fname.replace('.py', '.[FDOC].py')
        with open(path.join(fdir, fname), 'w') as docktored:
            docktored.write(funk_docktor(file.read(), clusters=False))


if __name__ == '__main__':
    main()
