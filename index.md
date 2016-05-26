---
layout: default
---

### Can you read ^\[\[1;32this^\[\[0m?

It ^\[\[1;31isn't^\[\[0m easy! To make output readable,
just respect my $TERM environment variable by
using
[tput](https://www.gnu.org/software/termutils/manual/termutils-2.0/html_chapter/tput_1.html#SEC4)
in scripts and
[curses](http://tldp.org/HOWTO/NCURSES-Programming-HOWTO/color.html)
in your programs.

The rest of this site demonstrates how to colorize output while respecting $TERM.

Please contribute your favoite language examples:

<iframe src="https://ghbtns.com/github-btn.html?user=respectmyterm&amp;repo=respectmyterm.github.io&amp;type=fork&amp;count=true&amp;size=large"
  allowtransparency="true" frameborder="0" scrolling="0" width="170px" height="30px"></iframe><br/>

Thank you for supporting Respect My Term. Tell your friends!

{% include sharing.html %}

### Shell Script

Instead of embedding terminal escape codes,
use `tput` to colorize output in scripts:

```sh
success() {
    tput setaf 2
    echo "$@"
    tput setaf 0
}

success 'Hello, World!'
```

This function works in any
[POSIX compatible shell](http://pubs.opengroup.org/onlinepubs/009604499/utilities/xcu_chap02.html).

You can learn more about `tput` from the
[GNU Term Utils Manual](https://www.gnu.org/software/termutils/manual/termutils-2.0/html_chapter/tput_toc.html)
or from the
[Linux Documentation Project](http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/c327.html).

### Python Program

Python supports [curses](https://docs.python.org/2/library/curses.html) out of the box:

```python
import curses

def success(s):
    colors = curses.tigetstr('setaf')

    def color(n):
        return curses.tparm(colors, n) if colors else ''

    print color(2) + s + color(0)

curses.setupterm()
success('Hello, World!')
```


### C Program

Of course

```c
#include <stdarg.h>
#include <stdio.h>
#include <term.h>

void success(const char *fmt, ...) {
    va_list argp;
    char *colors = tigetstr("setaf");

    if (colors)
        printf("%s", tparm(colors, 2));
    va_start(argp, fmt);
    vprintf(fmt, argp);
    va_end(argp);
    if (colors)
        printf("%s", tparm(colors, 0));
}

int main(void) {
    setupterm(NULL, 1, 0);
    success("Hello, World!\n");
}
```
