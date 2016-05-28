#!/bin/bin/env python
"""Test each of the "success" language implementations

Each implementation needs a file called "run.sh" that
is called by ``sh`` with ``TERM`` equal
different values, which are then tested by this programs.
"""
from __future__ import print_function
import glob
import os
import os.path
import subprocess

_EXPECT = 'Hello, World!\n'
_EXPECT = {
    'xterm': '\033[32m{}\033[30m'.format(_EXPECT),
    'dumb': _EXPECT,
}


_RUN_SH = 'run.sh'


def main():
    passed = 0
    total = 0
    prev_d = os.getcwd()
    for f in glob.glob('*/run.sh'):
        total += 1
        d = os.path.dirname(f)
        try:
            os.chdir(d)
            _test_one(os.path.basename(f))
            passed += 1
            msg = 'PASSED'
        except Exception as e:
            msg = 'FAILED'
            print('{}: exception: {} {}'.format(
                d, e, e.output if hasattr(e, 'output') else ''))
        finally:
            os.chdir(prev_d)
        print('{:>10}: {}'.format(d, msg))
    print('PASSED={} FAILED={}'.format(passed, total - passed))


def _test_one(script):
    env = os.environ.copy()
    for term, expect in _EXPECT.items():
        env['TERM'] = term
        out = subprocess.check_output(['sh', script], env=env)
        assert out == expect, \
            'expect={} out={}'.format(expect, out)

if __name__ == '__main__':
    main()
