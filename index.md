---
layout: default
---

### Can you read ^\[\[1;32it^\[\[0m?

It ^\[\[1;31isn't^\[\[0m easy! But it could be... All programs have to
do is respect my TERM environment variable.

Users run command line programs in different kinds of display environments,
some of which are "dumb". When programs disrespect $TERM by
outputting
[ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code),
we can't read ^\[\[1;32it^\[\[0m.

Stop frustrating your users. Make sure your output is always legible
by using
[tput](https://www.gnu.org/software/termutils/manual/termutils-2.0/html_chapter/tput_1.html#SEC4)
in scripts and
[curses](http://tldp.org/HOWTO/NCURSES-Programming-HOWTO/color.html)
in your programs.

#### Output Respectfully

The rest of this page is dedicated to how to format program output
while respecting $TERM.

Please contribute your favorite language examples:

<iframe src="https://ghbtns.com/github-btn.html?user=respectmyterm&amp;repo=respectmyterm.github.io&amp;type=fork&amp;count=true&amp;size=large"
  allowtransparency="true" frameborder="0" scrolling="0" width="170px" height="30px"></iframe><br/>

Thank you for Respecting My Term. Tell your friends!

{% include sharing.html %}

Apologies to non-POSIX command line users for using $TERM generically.
Your terminal environments deserve respect, too!

{% include sh/index.md %}
{% include python/index.md %}
{% include c/index.md %}

#### Work arounds

List of commands and flags to turn off color with various tools:

```
npm config set color false
```
