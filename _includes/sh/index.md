#### POSIX Shell

Instead of embedding terminal escape codes,
use `tput` to colorize output in scripts:

```sh
{% include sh/success.sh %}
```

This function works in any
[POSIX compatible shell](http://pubs.opengroup.org/onlinepubs/009604499/utilities/xcu_chap02.html).

You can learn more about `tput` from the
[GNU Term Utils Manual](https://www.gnu.org/software/termutils/manual/termutils-2.0/html_chapter/tput_toc.html)
or from the
[Linux Documentation Project](http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/c327.html).
