from __future__ import print_function
import curses

def success(s):
    colors = curses.tigetstr('setaf')

    def color(n):
        return curses.tparm(colors, n) if colors else ''

    print(color(2) + s + color(0))

curses.setupterm()
success('Hello, World!')
