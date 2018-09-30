from os import path, getcwd, remove
from pupy.decorations import tictoc
from subprocess import run, PIPE
from fdoc import funk_docktor
from time import time
from filecmp import cmp

test_files_dir = path.join(getcwd(), "test_files")

def test_basic():
    with open(path.join(test_files_dir, "fdoc_before_23lines.py"), "r") as before:
        before = before.read()
    with open(path.join(test_files_dir, "fdoc_after_basic_23lines.py"), "r") as after:
        after_baseline = after.read()
    after = funk_docktor(before, clusters=False)
    assert after_baseline == after

def test_basic_phillup():
    with open(path.join(test_files_dir, "fdoc_before_23lines.py"), "r") as before:
        before = before.read()
    with open(path.join(test_files_dir, "fdoc_after_basic_phillup_23lines.py"), "r") as after:
        after_baseline = after.read()
    after = funk_docktor(before, clusters=False, phillup=True)
    assert after_baseline == after


def test_basic_cli_no_inplace():
    cmd = 'python3 fdoc.py -f test_files/fdoc_before_23lines.py'
    baseline = path.join(getcwd(), 'test_files', 'fdoc_after_basic_23lines.py')
    doctored = path.join(getcwd(), 'test_files', 'fdoc_before_23lines.[FDOC].py')
    run(cmd, stderr=PIPE, stdout=PIPE, shell=True)
    assert cmp(baseline, doctored)
    remove(doctored)








def main():
    test_basic()
    test_basic_phillup()

if __name__ == '__main__':
    main()
